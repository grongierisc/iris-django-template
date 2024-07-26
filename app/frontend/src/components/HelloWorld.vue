<template>
  <div class="p-6 max-w-4xl mx-auto bg-white shadow-lg rounded-lg">
    <!-- Header -->
    <h1 class="text-4xl font-extrabold text-gray-900 mb-4">IRIS RAG</h1>
    
    <!-- Description -->
    <p class="text-lg text-gray-700 mb-6">
      Welcome to the <span class="font-semibold text-blue-600">RAG Application</span>, your comprehensive solution for managing conversations and documents with advanced AI-powered features.
    </p>
    <p class="text-lg text-gray-700 mb-6">
      Our application offers a seamless experience to query and manage documents. Whether you need to search through existing documents or add new ones, our powerful AI engine supports complex queries and delivers accurate responses.
    </p>
    <p class="text-lg text-gray-700 mb-6">
      <span class="font-semibold">Key Features:</span>
      <ul class="list-disc pl-5 mt-2">
        <li class="mb-2">Efficiently query documents with an intuitive interface.</li>
        <li class="mb-2">Add new documents and index them for easy retrieval.</li>
        <li class="mb-2">Delete existing documents with a few clicks.</li>
        <li class="mb-2">View and manage existing document names in real-time.</li>
      </ul>
    </p>
    <p class="text-lg text-gray-700">
      <span class="font-semibold">How It Works:</span> <br>
      - Start by entering your query or the text of a new document. <br>
      - If querying, select from existing documents or add a new one. <br>
      - The AI engine processes your request and provides relevant responses and citations. <br>
      - Manage your documents effortlessly by adding or deleting them as needed.
    </p>

    <h2 class="text-4xl font-extrabold text-gray-900 m-4">InterSystems IRIS Integration</h2>
    
    <p class="text-lg text-gray-700 mb-6">
      This application leverages <span class="font-semibold text-blue-600">InterSystems IRIS</span> as its backend database to efficiently store and manage documents. IRIS is a powerful, high-performance data platform known for its robust data management capabilities.
    </p>
    
    <p class="text-lg text-gray-700 mb-6">
      The application utilizes the <a href="https://github.com/grongierisc/iris-django-template/tree/main" class="text-blue-600 underline">IRIS Django template</a> for seamless integration with Django, allowing for effective interaction with the IRIS database. Additionally, it incorporates the <a href="https://github.com/caretdev/llama-iris" class="text-blue-600 underline">Llama-IRIS template</a>, which is built on SQLAlchemy, to handle advanced document management and querying.
    </p>
    
    <p class="text-lg text-gray-700 mb-6">
      The application employs <span class="font-semibold text-blue-600">llama_index</span> to manage the Retrieval-Augmented Generation (RAG) workflow. This includes handling queries, retrieving relevant documents, and generating responses based on the stored data.
    </p>
    
    <p class="text-lg text-gray-700 mb-6">
      Documents are stored in the IRIS database using the native <span class="font-semibold text-blue-600">iris $VECTOR</span> data type. This specialized data type supports efficient vector storage and retrieval, which is crucial for handling high-dimensional data used in machine learning and document processing.
    </p>
    
    <p class="text-lg text-gray-700 mb-6">
      The frontend of the application is built with <span class="font-semibold text-blue-600">Vue.js</span> and styled using <span class="font-semibold text-blue-600">Tailwind CSS</span>, providing a modern and responsive user interface for interacting with the application.
    </p>
    
    <p class="text-lg text-gray-700">
      <span class="font-semibold">Key Features:</span>
      <ul class="list-disc pl-5 mt-2">
        <li class="mb-2">Efficient document storage and retrieval using IRIS’s native $VECTOR data type.</li>
        <li class="mb-2">Integration with Django through the IRIS Django template for seamless backend operations.</li>
        <li class="mb-2">Advanced document management and querying capabilities with the Llama-IRIS template and SQLAlchemy.</li>
        <li class="mb-2">The Django framework handles data operations and document interactions with IRIS.</li>
        <li class="mb-2">Modern and responsive frontend built with Vue.js and styled with Tailwind CSS.</li>
        <li class="mb-2">Robust RAG workflow managed by llama_index for effective document handling and response generation.</li>
      </ul>
    </p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
}
</script>

<style scoped>
/* Custom styles are now replaced by Tailwind CSS classes */
</style>
