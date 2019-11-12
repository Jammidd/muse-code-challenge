<template>
  <div class="border my-2 rounded p-2 mx-4">
    <div class="flex flex-wrap items-top">
      <h4 class="text-sm font-semibold w-3/4">{{ item.title }}</h4>
      <p class="float-right italic text-sm font-light w-1/4 text-right">{{ item.locations[0] }}</p>
    </div>
    <h6 class="py-1 text-sm text-indigo-500 font-normal">{{ item.company.name }}</h6>
    <p class="mt-2 text-xs italic" v-html="summary"></p>
  </div>
</template>

<script>
export default {
  name: 'JobCard',
  props: ['item'],
  computed: {
    summary () {
      var cleanedDescription = this.item.description.replace(/<\/?[^>]+(>|$)/g, " ")
      return cleanedDescription.substring(0, 100) + '...'
    }
  }
}
</script>