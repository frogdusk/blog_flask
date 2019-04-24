var app = new Vue({
    el: '#app',
    data () {
      return {
        info: null
      }
    },
    mounted () {
      axios
        .get('http://127.0.0.1:5000')
        .then(response => (this.info = response))
    }
})