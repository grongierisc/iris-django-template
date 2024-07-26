<template>
  <div class="p-4 max-w-2xl mx-auto bg-white shadow-md rounded-lg">
    <!-- Header -->
    <h1 class="text-2xl font-bold mb-4">Query Document</h1>
    
    <!-- Query Input -->
    <div class="mb-4">
      <label for="query" class="block text-sm font-medium text-gray-700">Query</label>
      <input
        id="query"
        v-model="query"
        placeholder="Enter your query"
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      />
    </div>

    <!-- Document Name Input -->
    <div class="mb-4">
      <label for="document_name" class="block text-sm font-medium text-gray-700">Document Name</label>
      <input
        id="document_name"
        v-model="document_name"
        placeholder="Enter document name"
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      />
    </div>

    <!-- Document Textarea -->
    <div class="mb-4">
      <label for="document" class="block text-sm font-medium text-gray-700">Document</label>
      <textarea
        id="document"
        v-model="document"
        placeholder="Enter your document"
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        rows="4"
      ></textarea>
    </div>

    <!-- Existing Documents Multiselect-->
    <div class="mb-4">
      <label for="existing_documents" class="block text-sm font-medium text-gray-700">Existing Documents</label>
      <select
        id="existing_documents"
        v-model="selectedDocuments"
        multiple
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      >
        <option v-for="(name, index) in existing_document_names" :key="index" :value="name">
          {{ name }}
        </option>
      </select>
    </div>

    <!-- Submit Button -->
    <div class="mb-4">
      <button
        @click="submitQuery"
        class="w-full px-4 py-2 bg-blue-600 text-white font-semibold rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
      >
        Query
      </button>
    </div>

    <!-- Response Section -->
    <div v-if="responses" class="mb-4">
      <h2 class="text-xl font-semibold mb-2">Response:</h2>
      <p class="text-gray-800">{{ responses }}</p>
    </div>

    <!-- Citations Section -->
    <div v-if="citations" class="mb-4">
      <h2 class="text-xl font-semibold mb-2">Citations:</h2>
      <p class="text-gray-800">{{ citations }}</p>
    </div>

    <!-- Existing Document Names Section -->
    <div v-if="existing_document_names.length" class="mb-4">
      <h2 class="text-xl font-semibold mb-2">Existing Document Names:</h2>
      <ul class="list-disc pl-5">
        <li v-for="(name, index) in existing_document_names" :key="index" class="text-gray-800">{{ name }}</li>
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
      responses: '',
      citations: '',
      existing_document_names: [], 
      selectedDocuments: [],
    };
  },
  methods: {
    async submitQuery() {
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
          selected_documents: this.selectedDocuments || [],
        }),
      });
      const data = await response.json();
      this.responses = data.responses;
      this.citations = data.citations;
      this.existing_document_names = data.existing_document_names;
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
        // Set existing document names as an array
        this.existing_document_names = data.existing_document_names;
      } catch (error) {
        console.error('Error fetching existing document names:', error);
      }
    }
  },
  created() {
    this.fetchExistingDocumentNames();
  }
};
</script>

