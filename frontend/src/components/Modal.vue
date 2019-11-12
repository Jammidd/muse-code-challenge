<template>
  <div v-if="open">
    <div class="overlay" @click="close"></div>
    <div class="modal">
      <div class="modal-title p-4 border-b flex flex-wrap">
        <div class="w-3/4">
          <h3 class="text-lg font-bold">{{ job.title || 'Job Title' }}</h3>
          <p class="text-indigo-400">{{ job.company.name }}</p>
        </div>
        <p class="w-1/4 italic text-sm text-right">{{ job.location }}</p>
      </div>
      <div class="container mx-auto">
        <div class="modal-body" v-html="job.description"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'JobModal',
  mounted () {
    var self = this
    window.EventBus.$on('open:modal', (id) => { 
      self.fetchData(id)
    })
  },
  data () {
    return {
      open: false,
      job: {}
    }
  },
  methods: {
    close () {
      this.open = false
    },
    async fetchData (id) {
      var response = await this.$http.get(`/api/jobs/${id}`)

      this.job = response.data
      this.openModal()
    },
    openModal () {
      this.open = true
    }
  }
}
</script>