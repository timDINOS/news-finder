<template>
  <div>
    <SearchButton />
    <div class="news-entries">
      <div v-for="entry in filteredEntries" :key="entry.id" class="entry">
        <h3>{{ entry.title }}</h3>
        <p>{{ entry.description }}</p>
        <span>{{ entry.date }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    const response = await fetch('localhost:3000/news');
    const newsEntries = await response.json();
    return newsEntries;
  },
  computed: {
    filteredEntries() {
      const searchTerm = this.searchTerm.toLowerCase();
      if (!searchTerm) {
        return this.newsEntries;
      }
      return this.newsEntries.filter((entry) =>
        entry.title.toLowerCase().includes(searchTerm)
      );
    },
  },
};
</script>

<style>
.news-entries {
  display: flex;
  flex-wrap: wrap;
}

.entry {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
  width: 300px;
  min-height: 100px;
}
</style>