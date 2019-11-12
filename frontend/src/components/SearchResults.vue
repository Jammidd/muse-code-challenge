<template>
  <div class="result-grid my-4">
    <job-card v-for="job of jobs" :key="job.id" :item="job"></job-card>
    <div v-if="jobs.length == 0" class="text-center italic text-sm">no jobs found</div>
  </div>
</template>

<script>
import JobCard from '@/components/JobCard.vue'

export default {
  name: 'SearchResults',
  props: ['filters', 'query'],
  created () {
    this.fetchJobs()
  },
  data () {
    return {
      jobs: []
    }
  },
  methods: {
    async fetchJobs () {
      var url = '/api/jobs'

      var filterStr = ''
      if (this.query) {
        filterStr += `search=${this.query}&`
      }

      filterStr += this.generateFilterString()

      url += `?${filterStr}`

      var response = await this.$http.get(url)

      this.jobs = response.data
    },
    generateFilterString () {
      var str = ''
      if (this.filters.location) {
        str += `location=${this.filters.location}`
      }

      if (this.filters.category) {
        str += `&category=${this.filters.category}`
      }

      if (this.filters.levels.length > 0) {
        str += `&levels=${this.filters.levels.toString()}`
      }

      return str
    }
  },
  components: {
    JobCard
  },
  watch: {
    query () {
      this.fetchJobs()
    },
    filters () {
      this.fetchJobs()
    }
  }
}
</script>