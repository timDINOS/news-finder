<template>
    <div class="register">
        <h1>Login</h1>
        <form @submit.prevent="handleSubmit">
            <input v-model="name" v-validate="'required'" name="name" />
            <br />
            <br />
            <input v-model="age" v-validate="'required'" name="age"/>
            <br />
            <br />
            <input v-model="email" v-validate="'required'" name="email"/>
            <br />
            <br />
            <input v-model="username" v-validate="'required'" name="username"/>
            <br />
            <br />
            <input v-model="password" v-validate="'required'" name="password"/>
            <br />
            <br />
            <input v-model="retype_password" v-validate="'required'" name="retype password"/>
            <button type="submit">Sign Up</button>
        </form>
        <h3>Have an account? Log In Here.</h3>
        <br />
        <LoginButton />
    </div>
</template>


<script>
    import { LoginButton } from './components/LoginButton';
    export default {
        name: 'Register',
        components: {},
        data () {
            name: '',
            age: 0,
            email: '',
            username: '',
            password: '',
            retype_password: '',
            submitted: false
        },
        methods: {
            handleSubmit(e) {
                this.submitted = true;
                this.$validator.validate().then(res => {
                    if (res) {
                        this.register(this.name, this.age, this.email, this.username, this.password, this.retype_password);
                    }
                }) 
            }
        }
    }
</script>
