<template>
  <div class="p-4">
    <h1 class="text-center text-2xl font-bold">The Muse Job Search</h1>

    <div class="flex flex-wrap items-top mt-4">
      <div class="w-1/5">
        <job-filters @update="updateFilters"></job-filters>
      </div>
      <div class="w-2/3">
        <search-bar @update="updateQuery"></search-bar>

        <search-results :filters="filters" :query="query"></search-results>
      </div>
    </div>
    <job-modal></job-modal>
  </div>
</template>

<script>
import JobFilters from '@/components/JobFilters'
import JobModal from '@/components/Modal'
import SearchBar from '@/components/SearchBar'
import SearchResults from '@/components/SearchResults'

export default {
  name: 'MainView',
  data () {
    return {
      query: '',
      filters: {
        location: null,
        levels: [],
        category: null
      }
    }
  },
  methods: {
    updateFilters (filters) {
      this.filters = Object.assign({}, filters)
    },
    updateQuery (query) {
      this.query = query
    }
  },
  components: {
    JobFilters,
    JobModal,
    SearchBar,
    SearchResults
  }
}
</script>