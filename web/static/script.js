
// Atlas Web Interface - Interactive Functions
class AtlasWeb {
    constructor() {
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupFormHandlers();
    }

    setupEventListeners() {
        // Form submissions
        document.querySelectorAll('form').forEach(form => {
            form.addEventListener('submit', this.handleFormSubmit.bind(this));
        });

        // Search input
        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            searchInput.addEventListener('input', this.debounce(this.handleSearch.bind(this), 300));
        }

        // Content type filter
        const typeFilter = document.getElementById('type-filter');
        if (typeFilter) {
            typeFilter.addEventListener('change', this.handleTypeFilter.bind(this));
        }
    }

    setupFormHandlers() {
        // Content form
        const contentForm = document.getElementById('content-form');
        if (contentForm) {
            contentForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.addContent();
            });
        }

        // Search form
        const searchForm = document.getElementById('search-form');
        if (searchForm) {
            searchForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.performSearch();
            });
        }
    }

    async addContent() {
        const form = document.getElementById('content-form');
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;

        try {
            // Show loading state
            submitBtn.textContent = 'Adding...';
            submitBtn.disabled = true;

            const formData = new FormData(form);
            const data = {
                content: formData.get('content'),
                title: formData.get('title'),
                source: formData.get('source')
            };

            const response = await fetch('/api/content', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                this.showAlert('Content added successfully!', 'success');
                form.reset();

                // Refresh content list if on dashboard
                if (window.location.pathname === '/') {
                    await this.refreshContentList();
                }
            } else {
                this.showAlert(`Error: ${result.detail}`, 'error');
            }
        } catch (error) {
            this.showAlert('Network error: ' + error.message, 'error');
        } finally {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    }

    async performSearch() {
        const query = document.getElementById('search-query').value;
        if (!query.trim()) return;

        try {
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: query,
                    limit: 50
                })
            });

            const result = await response.json();

            if (response.ok) {
                this.displaySearchResults(result.results, query);
            } else {
                this.showAlert(`Search error: ${result.detail}`, 'error');
            }
        } catch (error) {
            this.showAlert('Search error: ' + error.message, 'error');
        }
    }

    displaySearchResults(results, query) {
        const resultsContainer = document.getElementById('search-results');
        if (!resultsContainer) return;

        if (results.length === 0) {
            resultsContainer.innerHTML = `
                <div class="alert alert-info">
                    No results found for "${query}"
                </div>
            `;
            return;
        }

        const resultsHtml = results.map(item => `
            <div class="content-item">
                <div class="content-title">${this.escapeHtml(item.title)}</div>
                <div class="content-meta">
                    <span class="content-type">${item.content_type || 'Unknown'}</span>
                    <span class="content-stage">Stage ${item.stage}</span>
                    <span>${new Date(item.created_at).toLocaleDateString()}</span>
                </div>
                ${item.ai_summary ? `<div class="content-summary">${this.escapeHtml(item.ai_summary)}</div>` : ''}
            </div>
        `).join('');

        resultsContainer.innerHTML = resultsHtml;
    }

    async refreshContentList() {
        try {
            const response = await fetch('/api/content?limit=10');
            const result = await response.json();

            if (response.ok) {
                this.updateContentList(result.results);
            }
        } catch (error) {
            console.error('Error refreshing content list:', error);
        }
    }

    updateContentList(contents) {
        const container = document.getElementById('recent-content');
        if (!container) return;

        const html = contents.map(item => `
            <div class="content-item">
                <div class="content-title">${this.escapeHtml(item.title)}</div>
                <div class="content-meta">
                    <span class="content-type">${item.content_type || 'Unknown'}</span>
                    <span class="content-stage">Stage ${item.stage}</span>
                    <span>${new Date(item.created_at).toLocaleDateString()}</span>
                </div>
                ${item.ai_summary ? `<div class="content-summary">${this.escapeHtml(item.ai_summary)}</div>` : ''}
            </div>
        `).join('');

        container.innerHTML = html || '<p>No content yet.</p>';
    }

    handleSearch(event) {
        const query = event.target.value;
        if (query.length > 2) {
            this.performSearch();
        }
    }

    handleTypeFilter(event) {
        const type = event.target.value;
        // Implement type filtering
        console.log('Filter by type:', type);
    }

    showAlert(message, type = 'info') {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type}`;
        alertDiv.textContent = message;

        const container = document.querySelector('.container');
        container.insertBefore(alertDiv, container.firstChild);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new AtlasWeb();
});
