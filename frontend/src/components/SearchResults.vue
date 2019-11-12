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
      var response = await this.$http.get('/api/jobs/')

      this.jobs = response.data
    }
  },
  components: {
    JobCard
  },
  watch: {
    query () {
      console.log(this.query)
    }
  }
}
</script>