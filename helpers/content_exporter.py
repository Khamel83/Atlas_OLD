"""
Content Export Engine for Atlas
Supports multiple output formats for knowledge management integration
"""

import json
import csv
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import yaml
from jinja2 import Environment, FileSystemLoader, Template


class ContentExporter:
    """Flexible content export engine supporting multiple formats"""

    def __init__(self, db_path: str = None, templates_dir: str = None):
        # Default to the podcast database if no path provided
        if db_path is None:
            db_path = str(
                Path(__file__).parent.parent / "data" / "podcasts" / "atlas_podcasts.db"
            )
        self.db_path = db_path
        self.templates_dir = (
            templates_dir or Path(__file__).parent.parent / "exports" / "templates"
        )
        self.jinja_env = Environment(loader=FileSystemLoader(str(self.templates_dir)))

    def export_content(
        self,
        content_ids: Optional[List[str]] = None,
        format_type: str = "markdown",
        filters: Optional[Dict] = None,
        output_path: str = None,
        template: str = None,
    ) -> Dict[str, Any]:
        """
        Export content in specified format

        Args:
            content_ids: Specific content IDs to export (optional)
            format_type: Output format (markdown, json, csv, obsidian, notion, anki)
            filters: Content filters (speaker, podcast, date_range, topic, etc.)
            output_path: Where to save exported content
            template: Custom template name (optional)

        Returns:
            Export result with status and file paths
        """

        # Get content based on IDs or filters
        if content_ids:
            content_data = self._get_content_by_ids(content_ids)
        else:
            content_data = self._get_filtered_content(filters or {})

        if not content_data:
            return {"status": "error", "message": "No content found for export"}

        # Apply format-specific processing
        formatted_content = self._format_content(content_data, format_type, template)

        # Write to output
        if output_path:
            output_files = self._write_export(
                formatted_content, format_type, output_path
            )
            return {
                "status": "success",
                "content_count": len(content_data),
                "files": output_files,
                "format": format_type,
            }
        else:
            return {
                "status": "success",
                "content_count": len(content_data),
                "data": formatted_content,
                "format": format_type,
            }

    def batch_export(
        self, export_configs: List[Dict], progress_callback: callable = None
    ) -> Dict[str, Any]:
        """
        Perform multiple exports in batch

        Args:
            export_configs: List of export configurations
            progress_callback: Optional progress tracking function

        Returns:
            Batch export results
        """
        results = []
        total = len(export_configs)

        for i, config in enumerate(export_configs):
            if progress_callback:
                progress_callback(
                    i, total, f"Exporting {config.get('format_type', 'unknown')}"
                )

            result = self.export_content(**config)
            results.append(result)

        return {
            "status": "completed",
            "total_exports": total,
            "successful": len([r for r in results if r["status"] == "success"]),
            "results": results,
        }

    def _get_content_by_ids(self, content_ids: List[str]) -> List[Dict]:
        """Get content by specific IDs"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row

            placeholders = ",".join("?" * len(content_ids))

            # Use the podcast database schema (episodes table)
            query = f"""
            SELECT 
                e.id,
                e.title,
                e.url as summary,
                e.publish_date as created_at,
                e.transcript_path as content,
                p.title as podcast_title,
                p.id as podcast_description,
                'transcript' as content_type,
                e.url as source_url,
                e.transcript_url
            FROM episodes e
            LEFT JOIN podcasts p ON e.podcast_id = p.id
            WHERE e.id IN ({placeholders}) AND e.transcript_path IS NOT NULL
            ORDER BY e.publish_date DESC
            """

            results = conn.execute(query, content_ids).fetchall()
            return [dict(row) for row in results]

    def _get_filtered_content(self, filters: Dict) -> List[Dict]:
        """Get content based on filters"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row

            # Build dynamic query based on filters using podcast database schema
            where_conditions = [
                "e.transcript_path IS NOT NULL"
            ]  # Only episodes with transcripts
            params = []

            if filters.get("podcast"):
                where_conditions.append("p.title LIKE ?")
                params.append(f"%{filters['podcast']}%")

            if filters.get("content_type"):
                # For podcast database, we only have podcast content
                if (
                    filters["content_type"] != "podcast"
                    and filters["content_type"] != "transcript"
                ):
                    return []  # No matches for other content types

            if filters.get("date_from"):
                where_conditions.append("e.publish_date >= ?")
                params.append(filters["date_from"])

            if filters.get("date_to"):
                where_conditions.append("e.publish_date <= ?")
                params.append(filters["date_to"])

            # Build query
            where_clause = " AND ".join(where_conditions) if where_conditions else "1=1"

            query = f"""
            SELECT 
                e.id,
                e.title,
                e.url as summary,
                e.publish_date as created_at,
                e.transcript_path as content,
                p.title as podcast_title,
                p.id as podcast_description,
                'transcript' as content_type,
                e.url as source_url
            FROM episodes e
            LEFT JOIN podcasts p ON e.podcast_id = p.id
            WHERE {where_clause}
            ORDER BY e.publish_date DESC
            """

            if filters.get("limit"):
                query += f" LIMIT {filters['limit']}"

            results = conn.execute(query, params).fetchall()
            return [dict(row) for row in results]

    def _format_content(
        self, content_data: List[Dict], format_type: str, template: str = None
    ) -> Any:
        """Format content based on export type"""

        if format_type == "json":
            return self._format_json(content_data)
        elif format_type == "csv":
            return self._format_csv(content_data)
        elif format_type == "markdown":
            return self._format_markdown(content_data, template)
        elif format_type == "obsidian":
            return self._format_obsidian(content_data)
        elif format_type == "notion":
            return self._format_notion(content_data)
        elif format_type == "anki":
            return self._format_anki(content_data)
        else:
            raise ValueError(f"Unsupported format type: {format_type}")

    def _format_json(self, content_data: List[Dict]) -> str:
        """Format as JSON with metadata"""
        export_data = {
            "export_timestamp": datetime.now().isoformat(),
            "content_count": len(content_data),
            "content": content_data,
        }
        return json.dumps(export_data, indent=2, default=str)

    def _format_csv(self, content_data: List[Dict]) -> str:
        """Format as CSV for spreadsheet analysis"""
        if not content_data:
            return ""

        # Get all unique keys for headers
        all_keys = set()
        for item in content_data:
            all_keys.update(item.keys())

        # Create CSV content
        import io

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=sorted(all_keys))
        writer.writeheader()

        for item in content_data:
            # Convert any non-string values to strings
            row = {k: str(v) if v is not None else "" for k, v in item.items()}
            writer.writerow(row)

        return output.getvalue()

    def _format_markdown(
        self, content_data: List[Dict], template: str = None
    ) -> List[Dict]:
        """Format as Markdown files with YAML frontmatter"""
        template_name = template or "markdown.jinja2"

        try:
            template_obj = self.jinja_env.get_template(template_name)
        except Exception:
            # Fallback to default markdown template
            template_obj = Template(self._get_default_markdown_template())

        formatted_files = []

        # Group content by main content item
        content_groups = self._group_content_by_item(content_data)

        for content_item, segments in content_groups.items():
            # Prepare data for template
            template_data = {
                "content": content_item,
                "segments": segments,
                "export_date": datetime.now().isoformat(),
                "total_segments": len(segments),
            }

            rendered_content = template_obj.render(**template_data)

            # Generate filename
            title = content_item.get("title", "untitled")
            safe_title = "".join(
                c for c in title if c.isalnum() or c in (" ", "-", "_")
            ).rstrip()
            filename = f"{safe_title[:50]}.md"

            formatted_files.append(
                {
                    "filename": filename,
                    "content": rendered_content,
                    "metadata": template_data,
                }
            )

        return formatted_files

    def _format_obsidian(self, content_data: List[Dict]) -> List[Dict]:
        """Format for Obsidian with wiki-links and tags"""
        formatted_files = []
        content_groups = self._group_content_by_item(content_data)

        for content_item, segments in content_groups.items():
            # Create Obsidian-specific formatting
            frontmatter = {
                "title": content_item.get("title", "Untitled"),
                "type": content_item.get("content_type", "unknown"),
                "source": content_item.get("source_url", ""),
                "podcast": content_item.get("podcast_title", ""),
                "created": content_item.get("created_at", ""),
                "speakers": list(
                    set(s["speaker"] for s in segments if s.get("speaker"))
                ),
                "topics": list(
                    set(s["topic_cluster"] for s in segments if s.get("topic_cluster"))
                ),
                "tags": [
                    f"#{content_item.get('content_type', 'content')}",
                    f"#{content_item.get('podcast_title', 'unknown').replace(' ', '_')}",
                ],
            }

            # Build content with wiki-links
            content_lines = [
                "---",
                yaml.dump(frontmatter, default_flow_style=False).strip(),
                "---",
                "",
                f"# {content_item.get('title', 'Untitled')}",
                "",
            ]

            if content_item.get("summary"):
                content_lines.extend(["## Summary", content_item["summary"], ""])

            if segments:
                content_lines.extend(["## Transcript Segments", ""])

                for segment in segments:
                    if segment.get("speaker") and segment.get("transcript_segment"):
                        speaker_link = f"[[{segment['speaker']}]]"
                        content_lines.append(
                            f"**{speaker_link}**: {segment['transcript_segment']}"
                        )
                        content_lines.append("")

            # Related content links
            if content_item.get("podcast_title"):
                content_lines.extend(
                    ["## Related", f"- [[{content_item['podcast_title']}]]", ""]
                )

            rendered_content = "\n".join(content_lines)

            # Safe filename for Obsidian
            title = content_item.get("title", "untitled")
            safe_title = "".join(
                c for c in title if c.isalnum() or c in (" ", "-", "_")
            ).rstrip()
            filename = f"{safe_title[:50]}.md"

            formatted_files.append(
                {
                    "filename": filename,
                    "content": rendered_content,
                    "metadata": frontmatter,
                }
            )

        return formatted_files

    def _format_notion(self, content_data: List[Dict]) -> Dict:
        """Format for Notion database import"""
        content_groups = self._group_content_by_item(content_data)

        # Prepare database entries
        database_entries = []

        for content_item, segments in content_groups.items():
            entry = {
                "Name": content_item.get("title", "Untitled"),
                "Type": content_item.get("content_type", ""),
                "Source": content_item.get("source_url", ""),
                "Podcast": content_item.get("podcast_title", ""),
                "Created": content_item.get("created_at", ""),
                "Summary": content_item.get("summary", ""),
                "Speakers": ", ".join(
                    set(s["speaker"] for s in segments if s.get("speaker"))
                ),
                "Topics": ", ".join(
                    set(s["topic_cluster"] for s in segments if s.get("topic_cluster"))
                ),
                "Segment_Count": len(segments),
                "Content_Length": len(content_item.get("content", "")),
                "Tags": f"{content_item.get('content_type', 'content')}, {content_item.get('podcast_title', 'unknown')}",
            }

            database_entries.append(entry)

        return {
            "database_schema": {
                "Name": "title",
                "Type": "select",
                "Source": "url",
                "Podcast": "select",
                "Created": "date",
                "Summary": "rich_text",
                "Speakers": "multi_select",
                "Topics": "multi_select",
                "Segment_Count": "number",
                "Content_Length": "number",
                "Tags": "multi_select",
            },
            "entries": database_entries,
        }

    def _format_anki(self, content_data: List[Dict]) -> List[Dict]:
        """Format as Anki flashcards"""
        flashcards = []
        content_groups = self._group_content_by_item(content_data)

        for content_item, segments in content_groups.items():
            # Create cards from key insights
            podcast_title = content_item.get("podcast_title", "Unknown Podcast")
            content_title = content_item.get("title", "Unknown Episode")

            # Question/Answer cards from segments
            for segment in segments:
                if segment.get("speaker") and segment.get("transcript_segment"):
                    segment_text = segment["transcript_segment"]
                    speaker = segment["speaker"]

                    # Create Q&A style cards for meaningful segments
                    if len(segment_text) > 100 and "?" in segment_text:
                        parts = segment_text.split("?", 1)
                        if len(parts) == 2:
                            question = parts[0].strip() + "?"
                            answer = parts[1].strip()

                            flashcards.append(
                                {
                                    "front": question,
                                    "back": answer,
                                    "speaker": speaker,
                                    "source": f"{podcast_title} - {content_title}",
                                    "topic": segment.get("topic_cluster", "General"),
                                    "deck": podcast_title,
                                    "tags": [
                                        content_item.get("content_type", "transcript"),
                                        speaker.replace(" ", "_"),
                                        segment.get("topic_cluster", "general").replace(
                                            " ", "_"
                                        ),
                                    ],
                                }
                            )

            # Summary cards
            if content_item.get("summary"):
                flashcards.append(
                    {
                        "front": f"What are the key points from: {content_title}?",
                        "back": content_item["summary"],
                        "speaker": "Summary",
                        "source": f"{podcast_title} - {content_title}",
                        "topic": "Summary",
                        "deck": podcast_title,
                        "tags": [
                            "summary",
                            content_item.get("content_type", "content"),
                        ],
                    }
                )

        return flashcards

    def _group_content_by_item(self, content_data: List[Dict]) -> Dict:
        """Group content by main content item (simplified for podcast database)"""
        groups = {}

        for row in content_data:
            content_id = row.get("id")
            if content_id not in groups:
                # Store main content item (no separate segments in current schema)
                groups[row] = (
                    []
                )  # Empty segments list since we don't have parsed segments yet

        return groups

    def _write_export(
        self, formatted_content: Any, format_type: str, output_path: str
    ) -> List[str]:
        """Write formatted content to files"""
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)

        created_files = []

        if format_type in ["markdown", "obsidian"]:
            # Multiple files
            for file_data in formatted_content:
                file_path = output_dir / file_data["filename"]
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(file_data["content"])
                created_files.append(str(file_path))

        elif format_type == "json":
            file_path = (
                output_dir
                / f"atlas_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(formatted_content)
            created_files.append(str(file_path))

        elif format_type == "csv":
            file_path = (
                output_dir
                / f"atlas_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            )
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(formatted_content)
            created_files.append(str(file_path))

        elif format_type == "notion":
            # JSON for Notion import
            file_path = (
                output_dir
                / f"notion_import_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(formatted_content, f, indent=2, default=str)
            created_files.append(str(file_path))

        elif format_type == "anki":
            # CSV format for Anki import
            file_path = (
                output_dir
                / f"anki_cards_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            )

            if formatted_content:
                with open(file_path, "w", encoding="utf-8", newline="") as f:
                    fieldnames = [
                        "front",
                        "back",
                        "speaker",
                        "source",
                        "topic",
                        "deck",
                        "tags",
                    ]
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()

                    for card in formatted_content:
                        # Convert tags list to string
                        card_data = card.copy()
                        card_data["tags"] = ", ".join(card.get("tags", []))
                        writer.writerow(card_data)

                created_files.append(str(file_path))

        return created_files

    def _get_default_markdown_template(self) -> str:
        """Default markdown template if no template file found"""
        return """---
title: {{ content.title }}
type: {{ content.content_type }}
source: {{ content.source_url }}
podcast: {{ content.podcast_title }}
created: {{ content.created_at }}
export_date: {{ export_date }}
---

# {{ content.title }}

{% if content.summary %}
## Summary
{{ content.summary }}
{% endif %}

{% if segments %}
## Transcript
{% for segment in segments %}
{% if segment.speaker and segment.transcript_segment %}
**{{ segment.speaker }}**: {{ segment.transcript_segment }}

{% endif %}
{% endfor %}
{% endif %}

---
*Exported from Atlas on {{ export_date }}*
"""
