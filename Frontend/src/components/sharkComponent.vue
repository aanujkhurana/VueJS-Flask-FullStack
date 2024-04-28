<template>
  <h1>{{ msg }}</h1>
</template>

<script>
import axios from 'axios'
export default {
  name: 'sharkComponent',
  data() {
    return {
      msg: ""
    }
  },
  methods: {
    getResponse() {
      const path = 'http://localhost:5001/'
      axios.get(path)
      .then((res)=>{
        console.log(res.data)
        this.msg = res.data
      })
      .catch((err) => {
      console.error('Axios error:', err.message);
      console.error('Error code:', err.code);
      console.error('Full error:', err);
      })
    }
  },
  created() {
    this.getResponse();
  },
} 
</script>