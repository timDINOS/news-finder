
<template>
    <Header />
    <LoginButton />
</template>


<script>
    import Header from './Header.vue'
    import LoginButton from './LoginButton.vue'
    export default {
        name: 'Home',
        components: {
            Header,
            LoginButton
        }
    }
</script>