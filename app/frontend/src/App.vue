<template>
  <div id="nav">
    <button @click="switchView('hello')">Hello World</button>
    <button @click="switchView('documents')">Document Manager</button>
  </div>
  <div id="app">
    <hello-world v-if="currentView === 'hello'"></hello-world>
    <document-manager v-if="currentView === 'documents'"></document-manager>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue';
import DocumentManager from '@/components/DocumentManager.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    DocumentManager,
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
