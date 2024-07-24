<template>
  <div id="nav">
    <button @click="switchView('hello')">Hello World</button>
    <button @click="switchView('documents')">Document Manager</button>
    <button @click="switchView('conversations')">Conversation Manager</button>
  </div>
  <div id="app">
    <hello-world v-if="currentView === 'hello'"></hello-world>
    <document-manager v-if="currentView === 'documents'"></document-manager>
    <conversation-manager v-if="currentView === 'conversations'"></conversation-manager>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue';
import DocumentManager from '@/components/DocumentManager.vue';
import ConversationManager from '@/components/ConversationManager.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    DocumentManager,
    ConversationManager,
  },
  data() {
    return {
      currentView: 'hello' // Default view
    };
  },
  methods: {
    switchView(view) {
      this.currentView = view;
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>
