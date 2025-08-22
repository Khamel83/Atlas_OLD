#!/usr/bin/env python3
"""
Search API for Atlas

This module provides RESTful API endpoints for the enhanced search functionality.
"""

from flask import Blueprint, jsonify, request
from helpers.enhanced_search import advanced_search
from helpers.search_engine import SearchEngine
import json

# Create blueprint for search API
search_bp = Blueprint('search', __name__, url_prefix='/api/search')

# Global search engine instance
try:
    search_engine = SearchEngine()
except Exception as e:
    search_engine = None

@search_bp.route('/', methods=['GET'])
@search_bp.route('/search', methods=['GET'])
def search():
    """
    Core search endpoint for Block 9 validation.
    
    Query Parameters:
        q (str): Search query
        limit (int, optional): Maximum number of results (default: 20)
        
    Returns:
        JSON response with search results
    """
    query = request.args.get('q', '')
    limit = request.args.get('limit', 20, type=int)
    
    if not query:
        return jsonify({'error': 'Query parameter "q" is required'}), 400
    
    try:
        # Use advanced search
        results = advanced_search(query, limit=limit)
        return jsonify({
            'query': query,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({'error': f'Search failed: {str(e)}'}), 500

@search_bp.route('/query', methods=['GET'])
def search_query():
    """
    Perform a search query
    
    Query Parameters:
        q (str): Search query
        limit (int, optional): Maximum number of results (default: 10)
        
    Returns:
        JSON response with search results
    """
    query = request.args.get('q', '')
    limit = request.args.get('limit', 10, type=int)
    
    if not query:
        return jsonify({'error': 'Query parameter "q" is required'}), 400
    
    try:
        if search_engine:
            results = search_engine.search(query, limit)
        else:
            results = []
        
        return jsonify({
            'query': query,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({'error': f'Search failed: {str(e)}'}), 500

@search_bp.route('/semantic', methods=['GET'])
def semantic_search():
    """
    Perform a semantic search
    
    Query Parameters:
        q (str): Search query
        limit (int, optional): Maximum number of results (default: 10)
        
    Returns:
        JSON response with semantic search results
    """
    query = request.args.get('q', '')
    limit = request.args.get('limit', 10, type=int)
    
    if not query:
        return jsonify({'error': 'Query parameter "q" is required'}), 400
    
    try:
        results = search_engine.semantic_search(query, limit)
        return jsonify({
            'query': query,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({'error': f'Semantic search failed: {str(e)}'}), 500

@search_bp.route('/filter', methods=['GET'])
def filtered_search():
    """
    Perform a filtered search
    
    Query Parameters:
        q (str): Search query
        limit (int, optional): Maximum number of results (default: 10)
        filters (str, optional): JSON-encoded filters
        
    Returns:
        JSON response with filtered search results
    """
    query = request.args.get('q', '')
    limit = request.args.get('limit', 10, type=int)
    
    # Parse filters from query parameter
    filters_param = request.args.get('filters', '{}')
    try:
        filters = json.loads(filters_param) if filters_param else {}
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON in filters parameter'}), 400
    
    if not query:
        return jsonify({'error': 'Query parameter "q" is required'}), 400
    
    try:
        results = search_engine.filter_search(query, filters, limit)
        return jsonify({
            'query': query,
            'filters': filters,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({'error': f'Filtered search failed: {str(e)}'}), 500

@search_bp.route('/documents', methods=['POST'])
def index_document():
    """
    Index a document
    
    Expected JSON format:
    {
        "id": "unique-document-id",
        "title": "Document Title",
        "content": "Document content...",
        "type": "article|podcast|youtube",
        "author": "Author Name",
        "metadata": {
            "category": "programming",
            "tags": ["python", "web-development"],
            ...
        }
    }
    
    Returns:
        JSON response with indexing status
    """
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'JSON data required'}), 400
    
    try:
        # Add to search engine
        doc_id = data.get('id', str(hash(data.get('content', ''))))
        content = data.get('content', '')
        metadata = data.get('metadata', {})
        
        search_engine.add_document(doc_id, content, metadata)
        
        # Add to indexer
        indexer.index_document(data)
        
        return jsonify({
            'status': 'success',
            'message': f'Document {doc_id} indexed successfully',
            'doc_id': doc_id
        })
    except Exception as e:
        return jsonify({'error': f'Indexing failed: {str(e)}'}), 500

@search_bp.route('/documents/<doc_id>', methods=['GET'])
def get_document(doc_id):
    """
    Retrieve a document by ID
    
    Args:
        doc_id (str): Document ID
        
    Returns:
        JSON response with document data
    """
    try:
        # Try to get from indexer first
        doc = indexer.get_document(doc_id)
        
        if doc:
            return jsonify(doc)
        else:
            # Document not found
            return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Retrieval failed: {str(e)}'}), 500

@search_bp.route('/documents/<doc_id>', methods=['PUT'])
def update_document(doc_id):
    """
    Update a document
    
    Args:
        doc_id (str): Document ID
        
    Expected JSON format:
    {
        "title": "Updated Title",
        "content": "Updated content...",
        ...
    }
    
    Returns:
        JSON response with update status
    """
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'JSON data required'}), 400
    
    try:
        # Update in indexer
        indexer.update_document(doc_id, data)
        
        # If content was updated, re-add to search engine
        if 'content' in data:
            content = data.get('content', '')
            metadata = data.get('metadata', {})
            search_engine.add_document(doc_id, content, metadata)
        
        return jsonify({
            'status': 'success',
            'message': f'Document {doc_id} updated successfully'
        })
    except Exception as e:
        return jsonify({'error': f'Update failed: {str(e)}'}), 500

@search_bp.route('/documents/<doc_id>', methods=['DELETE'])
def delete_document(doc_id):
    """
    Delete a document
    
    Args:
        doc_id (str): Document ID
        
    Returns:
        JSON response with deletion status
    """
    try:
        # Remove from indexer
        indexer.remove_document(doc_id)
        
        # Note: In a real implementation, we would also remove from search engine
        # For simplicity, we're not implementing that here
        
        return jsonify({
            'status': 'success',
            'message': f'Document {doc_id} deleted successfully'
        })
    except Exception as e:
        return jsonify({'error': f'Deletion failed: {str(e)}'}), 500

@search_bp.route('/stats', methods=['GET'])
def get_search_stats():
    """
    Get search system statistics
    
    Returns:
        JSON response with search system statistics
    """
    try:
        # Get search engine stats
        search_stats = search_engine.get_index_stats()
        
        # Get indexer stats
        indexer_stats = indexer.get_index_stats()
        
        return jsonify({
            'search_engine': search_stats,
            'indexer': indexer_stats,
            'timestamp': '2023-05-01T12:00:00Z'  # In a real implementation, this would be current time
        })
    except Exception as e:
        return jsonify({'error': f'Stats retrieval failed: {str(e)}'}), 500

@search_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    
    Returns:
        JSON response with health status
    """
    return jsonify({
        'status': 'healthy',
        'service': 'search-api',
        'timestamp': '2023-05-01T12:00:00Z'  # In a real implementation, this would be current time
    })

# Error handlers
@search_bp.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@search_bp.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

def register_search_routes(app):
    """
    Register search routes with the Flask app
    
    Args:
        app (Flask): Flask application instance
    """
    app.register_blueprint(search_bp)

def initialize_search_system(documents=None):
    """
    Initialize the search system with sample documents
    
    Args:
        documents (List[Dict], optional): Documents to index initially
    """
    global search_engine, indexer
    
    # Create new instances
    search_engine = EnhancedSearchEngine()
    indexer = SearchIndexer()
    
    # Index sample documents if provided
    if documents:
        print(f"Indexing {len(documents)} sample documents...")
        search_engine.build_index(documents)
        
        # Also index in the SQL-based indexer
        for doc in documents:
            indexer.index_document(doc)
        
        print("Search system initialized with sample documents")
    else:
        print("Search system initialized")

def create_flask_app():
    """Create Flask app with search API endpoints"""
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(search_bp)
    return app

def main():
    """Example usage"""
    print("Search API endpoints registered")
    print("Available endpoints:")
    print("  GET /api/search/query?q=<query>")
    print("  GET /api/search/semantic?q=<query>")
    print("  GET /api/search/filter?q=<query>&filters=<json>")
    print("  POST /api/search/documents")
    print("  GET /api/search/documents/<doc_id>")
    print("  PUT /api/search/documents/<doc_id>")
    print("  DELETE /api/search/documents/<doc_id>")
    print("  GET /api/search/stats")
    print("  GET /api/search/health")

if __name__ == "__main__":
    main()