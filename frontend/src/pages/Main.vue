<template>
  <div class="p-4">
    <h1 class="text-center text-2xl font-bold">The Muse Job Search</h1>

    <div class="flex flex-wrap items-top mt-4">
      <div class="w-1/5">
        <job-filters></job-filters>
      </div>
      <div class="w-2/3">
        <search-bar @update="updateQuery"></search-bar>

        <search-results :filters="filters" :query="query"></search-results>
      </div>
    </div>
  </div>
</template>

<script>
import JobFilters from '@/components/JobFilters'
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
    updateQuery (query) {
      this.query = query
    }
  },
  components: {
    JobFilters,
    SearchBar,
    SearchResults
  }
}
</script>