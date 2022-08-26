
<template>
    <Header />
    <LoginButton />
    <SignUpButton />
    <h1>
        Welcome!
    </h1>
    <h3>
        Log In and Start Searching for news!
    </h3>
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