<script setup>
import { ref } from 'vue';

const firstName = ref("")
const lastName = ref("")
const dateOfBirth = ref(new Date())
const gender = ref("male")
const address = ref("")
const phone = ref("")
const email = ref("")
const emergencyContact = ref("")

const onSubmit = () => {
    console.log("First Name:", firstName.value)
    console.log("Last Name:", lastName.value)
    console.log("Date of Birth:", dateOfBirth.value)
    console.log("Gender:", gender.value)
    console.log("Address:", address.value)
    console.log("Phone:", phone.value)
    console.log("Email:", email.value)
    console.log("Emergency Contact:", emergencyContact.value)
    
}

</script>

<template>
    <div>

        <h2>Create Patients</h2>
        <form>
            <div class="form-row">
                <label>first name: </label>
                <input v-model="firstName" type="text" id="first-name"/>
            </div>
            <div class="form-row">
                <label>last name: </label>
                <input v-model="lastName" type="text" id="last-name"/>
            </div>
            <div class="form-row">
                <label>date of birth: </label>
                <input v-model="dateOfBirth" type="date" id="date-of-birth"/>
            </div>
            <div class="form-row">
                <label>gender: </label>
                <select v-model="gender" name="gender" id="gender">
                    <option value="male">male</option>
                    <option value="female">female</option>
                </select>
            </div>
            <div class="form-row">
                <label>address: </label>
                <input v-model="address" type="text" id="address"/>
            </div>
            <div class="form-row">
                <label>phone: </label>
                <input v-model="phone" type="text" id="phone"/>
            </div>
            <div class="form-row">
                <label>email: </label>
                <input v-model="email" type="text" id="email"/>
            </div>
            <div class="form-row">
                <label>emergency contact: </label>
                <input v-model="emergencyContact" type="text" id="emergency-contact"/>
            </div>
        </form>
        <button v-on:click="onSubmit()">submit</button>
        
    </div>
</template>


<style scoped>
.form-row {
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    margin-bottom: 1rem;
}
</style>