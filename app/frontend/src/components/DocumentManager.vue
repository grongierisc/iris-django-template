<template>
  <div class="max-w-4xl mx-auto px-4 py-6">
    <!-- Header -->
    <h1 class="text-3xl font-extrabold mb-6 text-gray-900">Query and Manage Documents</h1>

    <!-- Model Name Dropdown -->
    <div class="mb-6">
      <label for="model_name" class="block text-gray-700 text-sm font-bold mb-2">Model Name</label>
      <select
        id="model_name"
        v-model="model_name"
        class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 rounded shadow-sm focus:outline-none focus:shadow-outline"
      >
        <option value="gpt-4">GPT-4</option>
        <option value="gpt-3.5-turbo">GPT-3.5-turbo</option>
        <option value="gpt-4o">GPT-4o</option>
        <option value="gpt-4o-mini">GPT-4o-mini</option>
      </select>
    </div>

    <!-- Temperature Input -->
    <div class="mb-6">
      <label for="temperature" class="block text-gray-700 text-sm font-bold mb-2">Temperature (0-2)</label>
      <input
        id="temperature"
        type="number"
        v-model.number="temperature"
        min="0"
        max="2"
        step="0.1"
        class="block w-full bg-white border border-gray-400 px-4 py-2 rounded shadow-sm focus:outline-none focus:shadow-outline"
        placeholder="Enter temperature"
      />
    </div>

    <!-- Query Input -->
    <div class="mb-6 relative">
      <label for="query" class="block text-gray-700 text-sm font-bold mb-2">Query</label>
      <input
        id="query"
        v-model="query"
        placeholder="Enter your query"
        class="block w-full bg-white border border-gray-400 px-4 py-2 rounded shadow-sm focus:outline-none focus:shadow-outline"
      />
      <button @click="clearQuery" class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-600 hover:text-gray-900">
        &#x2715;
      </button>
    </div>

    <!-- Document Name Input -->
    <div class="mb-6 relative">
      <label for="document_name" class="block text-gray-700 text-sm font-bold mb-2">Document Name</label>
      <input
        id="document_name"
        v-model="document_name"
        placeholder="Enter document name"
        class="block w-full bg-white border border-gray-400 px-4 py-2 rounded shadow-sm focus:outline-none focus:shadow-outline"
      />
      <button @click="clearDocumentName" class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-600 hover:text-gray-900">
        &#x2715;
      </button>
    </div>

    <!-- Document Textarea -->
    <div class="mb-6 relative">
      <label for="document" class="block text-gray-700 text-sm font-bold mb-2">Document</label>
      <textarea
        id="document"
        v-model="document"
        placeholder="Enter your document text"
        class="block w-full bg-white border border-gray-400 px-4 py-2 rounded shadow-sm focus:outline-none focus:shadow-outline"
        rows="6"
      ></textarea>
      <button @click="clearDocument" class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-600 hover:text-gray-900">
        &#x2715;
      </button>
    </div>

    <!-- Existing Documents Multiselect -->
    <div class="mb-6">
      <label for="existing_documents" class="block text-gray-700 text-sm font-bold mb-2">Existing Documents</label>
      <select
        id="existing_documents"
        v-model="selectedDocuments"
        multiple
        class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 rounded shadow-sm focus:outline-none focus:shadow-outline"
      >
        <option v-for="(name, index) in existing_document_names" :key="index" :value="name">
          {{ name }}
        </option>
      </select>
    </div>

    <!-- Submit Button -->
    <div class="mb-6">
      <button
        @click="submitQuery"
        class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Query
      </button>
    </div>

    <!-- Clear All Button -->
    <div class="mb-6">
      <button
        @click="clearAll"
        class="w-full bg-gray-600 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Clear All
      </button>
    </div>

    <!-- Delete Button -->
    <div class="mb-6">
      <button
        @click="deleteDocuments"
        class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Delete Selected Documents
      </button>
    </div>

    <!-- Response Section -->
    <div v-if="responses" class="mb-6">
      <h2 class="text-2xl font-semibold mb-2 text-gray-900">Responses:</h2>
      <div v-for="(response, document_name) in responses" :key="document_name" class="mb-4">
        <h3 class="text-lg font-semibold text-gray-800">{{ document_name }}</h3>
        <p class="text-gray-700 mb-2">{{ response.response }}</p>
        <div v-if="response.citations" class="text-gray-600">
          <h4 class="text-md font-semibold mb-1">Citations:</h4>
          <div v-for="(citation, index) in parseCitations(response.citations)" :key="index" class="mb-2 p-2 border border-gray-200 rounded-lg">
            <p>{{ citation }}</p>
          </div>
        </div>
        <hr class="my-4 border-gray-300" />
      </div>
    </div>

    <!-- Existing Document Names Section -->
    <div v-if="existing_document_names.length" class="mb-6">
      <h2 class="text-2xl font-semibold mb-2 text-gray-900">Existing Document Names:</h2>
      <ul class="list-disc pl-5 text-gray-800">
        <li v-for="(name, index) in existing_document_names" :key="index">{{ name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import VueCookies from 'vue-cookies';

export default {
  data() {
    return {
      query: '',
      document: '',
      document_name: '',
      model_name: 'gpt-4o-mini', // Default model name
      temperature: .5, // Default temperature
      responses: {},  // Should be an object to store document names as keys
      existing_document_names: [], 
      selectedDocuments: [],
    };
  },
  methods: {
    async submitQuery() {
      try {
        const response = await fetch('/django/api/documents/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': VueCookies.get('csrftoken'),
          },
          body: JSON.stringify({
            query_text: this.query,
            document_text: this.document,
            document_name: this.document_name,
            model_name: this.model_name,
            temperature: this.temperature,
            selected_documents: this.selectedDocuments || [],
          }),
        });
        const data = await response.json();
        this.responses = data.responses;
        this.existing_document_names = data.existing_document_names;
      } catch (error) {
        console.error('Error submitting query:', error);
        alert('An unexpected error occurred.');
      }
    },
    
    async fetchExistingDocumentNames() {
      try {
        const response = await fetch('/django/api/document_names/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': VueCookies.get('csrftoken'),
          },
        });
        const data = await response.json();
        this.existing_document_names = data.existing_document_names;
      } catch (error) {
        console.error('Error fetching existing document names:', error);
      }
    },
    
    async deleteDocuments() {
      if (this.selectedDocuments.length === 0) {
        alert('Please select documents to delete.');
        return;
      }
      
      if (!confirm('Are you sure you want to delete the selected documents?')) {
        return;
      }
      
      try {
        const response = await fetch('/django/api/documentsdelete/', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': VueCookies.get('csrftoken'),
          },
          body: JSON.stringify({ document_names: this.selectedDocuments }),
        });
        const data = await response.json();
        if (response.ok) {
          alert('Documents deleted successfully.');
          this.selectedDocuments = [];
          this.fetchExistingDocumentNames();  // Refresh the list of documents
        } else {
          alert('Error deleting documents: ' + data.error);
        }
      } catch (error) {
        console.error('Error deleting documents:', error);
        alert('An unexpected error occurred.');
      }
    },

    parseCitations(citations) {
      let splitCitations = citations.split('\n> Source ');
      let filteredCitations = splitCitations.filter(citation => citation.trim());
      let mappedCitations = filteredCitations.map((citation, index) => {
        if (index === 0) {
          return citation.trim();
        } else {
          return '> Source ' + citation.trim();
        }
      });
      return mappedCitations;
    },

    clearQuery() {
      this.query = '';
    },

    clearDocumentName() {
      this.document_name = '';
    },

    clearDocument() {
      this.document = '';
    },

    clearAll() {
      this.query = '';
      this.document = '';
      this.document_name = '';
      this.selectedDocuments = [];
      this.responses = {};
    }
  },
  created() {
    this.fetchExistingDocumentNames();
  }
};
</script>

<style scoped>
/* Disabled button style */
button:disabled {
  background-color: #999;
  cursor: not-allowed;
}
</style>
