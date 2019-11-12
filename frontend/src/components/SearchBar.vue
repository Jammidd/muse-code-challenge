<template>
  <div>
    <input
      ref="search"
      class="border rounded px-4 py-1 w-full"
      type='text' 
      v-model="query" 
      placeholder="Search job titles" />
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  mounted () {
    var self = this
    this.$refs.search.onkeyup = function () {
      clearTimeout(self.timer)
      self.timer = setTimeout(() => {self.$emit('update', self.query)}, self.typingDelay)
    }

    this.$refs.search.onkeydown = function () {
      clearTimeout(self.timer)
    }
  },
  data () {
    return {
      query: '',
      timer: null,
      typingDelay: 3000
    }
  }
}
</script>