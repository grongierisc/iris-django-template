<template>
    <div>
      <h1>Conversation Manager</h1>
      <textarea v-model="prompt" placeholder="Enter your prompt"></textarea>
      <button @click="sendQuery">Send Query</button>
      <div v-if="response">
        <p>{{ response }}</p>
      </div>
      <div v-for="document in relatedDocuments" :key="document.id">
        <p>{{ document.title }} - {{ document.content }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        prompt: '',
        response: '',
        relatedDocuments: [],
      };
    },
    methods: {
      async sendQuery() {
        const response = await fetch('/api/conversations/query/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            prompt: this.prompt,
            model_name: this.selectedModel,
          }),
        });
        const data = await response.json();
        this.response = data.response;
        this.relatedDocuments = data.documents;
      },
    },
  };
  </script>
  