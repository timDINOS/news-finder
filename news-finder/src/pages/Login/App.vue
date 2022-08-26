

<template>
    <div class="login">
        <h1>Login</h1>
        <form @submit="login">
            <input v-model="username" placeholders="username" />
            <br />
            <br />
            <input v-model="password" placeholders="password" type="password"/>
            <br />
            <br />
            <button type="submit">Login</button>
        </form>
        <h3>Don't have an account? Sign Up Here.</h3>
        <br />
        <SignUpButton />
    </div>
</template>


<script>
    import SignUpButton from './SignUpButton.vue';
    export default {
        name: "Login",
        components: {},
        data: () => {
            return {
                username: "",
                password: ""
            };
        },
        methods: {
            async login(e) {
                e.preventDefault();
                await fetch("", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        username: this.username, 
                        password: this.password
                    }),
                });

                this.$router.push("/");
            };
        },
    };
</script>