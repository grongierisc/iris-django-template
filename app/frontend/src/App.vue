<template>
  <div id="app">
    <hello-world ></hello-world>
    <document-manager></document-manager>
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
