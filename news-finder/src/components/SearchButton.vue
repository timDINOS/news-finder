<script>
    export default {
    name: "SearchButton",
    components: {},
    data() {
        return {
        searchTerm: "",
        newsEntries: [],
        };
    },
    methods: {
        async fetchNewsEntries() {
        const response = await fetch("localhost:3000/news");
        const newsEntries = await response.json();
        this.newsEntries = newsEntries;
        },
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
    mounted() {
        this.fetchNewsEntries();
    },
    };
</script>


<template>
    <div class="search-button">
        <input
        type="text"
        v-model="searchTerm"
        placeholder="Search for news"
        />
        <button>Search</button>
    </div>
</template>


<style>
    .search-button {
        color: gray;
    }
</style>
