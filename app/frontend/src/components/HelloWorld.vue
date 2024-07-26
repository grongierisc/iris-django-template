<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      Welcome to our RAG Application. This is your hub for managing conversations and documents.<br>
      Explore the features and get started with your AI-powered tasks.
    </p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<style scoped>
.hello {
  padding: 20px;
  background-color: #e7cdb3;
  color: #253e58;
}

h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #3F7865;
}
</style>
