<template>
  <div class="filters px-4">
    <h5 class="border-b pb-2 uppercase text-sm">Filters</h5>

    <div class="mt-4">
      <label class="text-xs block uppercase text-gray-500 font-bold my-1">Location</label>
      <input class="w-full border rounded px-2 py-1 text-sm font-light" type="text" v-model="filters.location" placeholder="select location" />
    </div>

    <div class="mt-8">
      <label class="text-xs block uppercase text-gray-500 font-bold my-1">Level(s)</label>
      <div class="block">
        <label><input class="mr-2" type="checkbox" v-model="filters.levels" value="I" />Internship</label>
      </div>
      <div class="block">
        <label><input class="mr-2" type="checkbox" v-model="filters.levels" value="E" />Entry Level</label>
      </div>
      <div class="block">
        <label><input class="mr-2" type="checkbox" v-model="filters.levels" value="M" />Mid Level</label>
      </div>
      <div class="block">
        <label><input class="mr-2" type="checkbox" v-model="filters.levels" value="S" />Senior Level</label>
      </div>
    </div>

    <div class="mt-8">
      <label class="text-xs block uppercase text-gray-500 font-bold my-1">Category</label>
      <input class="w-full border rounded px-2 py-1 text-sm font-light" type="text" v-model="filters.category" placeholder="select category" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'JobFilters',
  data () {
    return {
      filters: {
        location: null,
        levels: [],
        category: null
      }
    }
  }
}
</script>