<template>
    <div>
      <h1>Document Manager</h1>
      <input type="file" @change="handleFileUpload" />
      <textarea v-model="plainText" placeholder="Paste plain text here"></textarea>
      <button @click="addPlainText">Add Text</button>
      <button @click="convertToEmbeddings">Convert to Embeddings</button>
      <select v-model="selectedModel">
        <option v-for="model in models" :key="model" :value="model">{{ model }}</option>
      </select>
      <button @click="loadModel">Load Model</button>
      <button @click="queryDatabase">Query Database</button>
      <div v-for="document in documents" :key="document.id">
        <p>{{ document.title }} - {{ document.content }}</p>
        <button @click="deleteDocument(document.id)">Delete</button>
      </div>
      <div v-for="conversation in conversations" :key="conversation.id">
        <p>{{ conversation.prompt }}</p>
        <p>{{ conversation.response }}</p>
        <div v-for="doc in conversation.documents" :key="doc.id">
          <p>{{ doc.title }} - {{ doc.content }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        documents: [],
        conversations: [],
        file: null,
        plainText: '',
        selectedModel: '',
        models: ['model1', 'model2'], // Add model names here
      };
    },
    methods: {
      handleFileUpload(event) {
        this.file = event.target.files[0];
      },
      addPlainText() {
        // Implement plain text addition logic
        const plainTextDocument = {
          title: 'Plain Text',
          content: this.plainText,
        };
        this.documents.push(plainTextDocument);
        this.plainText = '';
      },
      convertToEmbeddings() {
        // Implement file reading, embedding conversion, and API call to save the document
        if (this.file) {
          const reader = new FileReader();
          reader.onload = async (e) => {
            const content = e.target.result;
            const document = { title: this.file.name, content: content };
            await this.saveDocument(document);
          };
          reader.readAsText(this.file);
        }
      },
      async saveDocument(document) {
        // Save document via API
        const response = await fetch('django/api/documents/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(document),
        });
        const newDocument = await response.json();
        this.documents.push(newDocument);
      },
      loadModel() {
        // Implement model loading logic
      },
      async queryDatabase() {
        const response = await fetch('django/api/conversations/query/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            prompt: this.plainText,
            model_name: this.selectedModel,
          }),
        });
        const newConversation = await response.json();
        this.conversations.push(newConversation);
      },
      async deleteDocument(id) {
        await fetch(`django/api/documents/${id}/`, {
          method: 'DELETE',
        });
        this.documents = this.documents.filter(doc => doc.id !== id);
      },
    },
    async created() {
      const docResponse = await fetch('django/api/documents/');
      this.documents = await docResponse.json();
      const convoResponse = await fetch('django/api/conversations/');
      this.conversations = await convoResponse.json();
    },
  };
  </script>
  