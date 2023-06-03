<template>
    <div class="header">
        <h1>News Finder</h1>
        <LoginButton />
        <SignUpButton />
        <News />
    </div>
</template>

<script>
    import LoginButton from './LoginButton'
    import SignUpButton from './SignUpButton'
    export default {
        name: "Header",
        components: {
            LoginButton,
            SignUpButton
        }
    }
</script>

<style>
    .header {
        text-align: left;
        color: green;
        font-size: 25px;
    }

    .LoginButton {
        position: absolute;
        top: 10;
        right: 4;
    }

    .SignUpButton {
        position: absolute;
        top: 10;
        right: 7;
    }
</style>