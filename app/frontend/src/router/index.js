import { createRouter, createWebHistory } from 'vue-router';
import DocumentManager from '../components/DocumentManager.vue';
import ConversationManager from '../components/ConversationManager.vue';
import HelloWorld from '@/components/HelloWorld.vue';

const routes = [
  { path: '/', component: HelloWorld },
  { path: '/documents', component: DocumentManager },
  { path: '/conversations', component: ConversationManager },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
