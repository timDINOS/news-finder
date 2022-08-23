
<template>
    <Header />
    <LoginButton />
    <SignUpButton />
</template>


<script>
    import Header from './Header.vue'
    import LoginButton from './LoginButton.vue'
    import SignUpButton from './SignUpButton.vue'
    export default {
        name: 'Home',
        components: {
            Header,
            LoginButton,
            SignUpButton
        }
    }
</script>