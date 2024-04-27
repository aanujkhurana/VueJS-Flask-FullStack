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
      const path = 'http://localhost:5000/'
      axios.get(path)
      .then((res)=>{
        console.log(res.data)
        this.msg = res.data
      })
      .catch((err)=>{
        console.error(err)
      })
    }
  },
  created() {
    this.getResponse();
  },
} 
</script>