<template>
  <v-app>
    <v-app-bar
        class="grey lighten-3"
        app
        color="white"
        flat
    >
      <v-container class="fill-height">
        <v-spacer></v-spacer>
        <v-btn class="mr-0" @click="RegisterShow=true; LoginShow=false; SignedUpShow=false; SignedInShow=false; InvalidPasswordShow=false;" text>
          Регистрация
        </v-btn>
        <v-btn class="mr-0" @click="RegisterShow=false; LoginShow=true; SignedUpShow=false; SignedInShow=false; InvalidPasswordShow=false;" text>
          Вход
        </v-btn>
      </v-container>
    </v-app-bar>

    <v-container class="align-content-center">
      <v-form
          v-if="RegisterShow"
          ref="form1"
          v-model="validReg"
          lazy-validation
      >
        <v-text-field
            v-model="name"
            :counter="30"
            :rules="nameRulesReg"
            label="Имя"
            required
        ></v-text-field>

        <v-text-field
            v-model="email"
            :rules="emailRulesReg"
            label="E-mail"
            required
        ></v-text-field>

        <v-text-field
            type="password"
            v-model="password"
            :rules="passwordRulesReg"
            label="Пароль"
            required
        ></v-text-field>

        <v-select
            v-model="select"
            :items="items"
            :rules="[v => !!v || 'Необходимо выбрать роль']"
            label="Роль"
            required
        ></v-select>

        <v-select
            v-if="select === 'Репетитор'"
            v-model="selectSubj"
            :items="subjects"
            :rules="[v => !!v || 'Для преподавателя необходимо выбрать предмет']"
            label="Предмет"
            required
        ></v-select>

        <v-checkbox
            v-model="checkbox"
            :rules="[v => !!v || 'You must agree to continue!']"
            label="Согласен с условиями использования данного ресурса"
            required
        ></v-checkbox>

        <v-btn
            :disabled="!validReg"
            color="success"
            class="mr-4"
            @click="register"
        >
          Зарегестрироваться
        </v-btn>

        <v-btn
            color="error"
            class="mr-4"
            @click="resetRegister"
        >
          Сбросить
        </v-btn>

      </v-form>
    </v-container>

    <v-container class="align-content-center">
      <v-form
          v-if="LoginShow"
          ref="form2"
          v-model="validLog"
          lazy-validation
      >
        <v-text-field
            type="email"
            v-model="email"
            :rules="emailRulesLog"
            label="E-mail"
            required
        ></v-text-field>

        <v-text-field
            type="password"
            v-model="password"
            :rules="passwordRulesLog"
            label="Пароль"
            required
        ></v-text-field>

        <v-btn
            :disabled="!validLog"
            color="success"
            class="rounded-lg mr-4"
            @click="login"
        >
          Войти
        </v-btn>

        <v-btn
            color="error"
            class="rounded-lg mr-4"
            @click="resetLogin"
        >
          Сбросить
        </v-btn>
      </v-form>
      <v-banner v-if="SignedInShow">Вы успешно зарегестрировались. Представьте, что тут случился переход на вашу основную страницу</v-banner>
      <v-banner v-if="SignedUpShow">Вы успешно вошли в аккаунт. Представьте, что тут случился переход на вашу основную страницу</v-banner>
      <v-card-text v-if="InvalidPasswordShow" style="color: red">
        Неверный e-mail или пароль
      </v-card-text>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios';
export default {
  name: 'LogRegForm',
  data: () => ({
    RegisterShow: true,
    LoginShow: false,
    SignedUpShow: false,
    SignedInShow: false,
    InvalidPasswordShow: false,
    SubjShow: false,
    validReg: true,
    validLog: true,
    name: '',
    nameRulesReg: [
      v => !!v || 'Name is required',
      v => (v && v.length <= 30) || 'Name must be less than 30 characters',
    ],
    email: '',
    emailRulesReg: [
      v => !!v || 'E-mail is required',
      v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    password: '',
    passwordRulesReg: [
      v => !!v || 'Password is required',
      v => /^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d).*$/.test(v) || 'Password must contain 8 characters and at least one number and one letter'
    ],
    emailRulesLog: [
      v => !!v || 'E-mail is required',
      // v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    passwordRulesLog: [
      v => !!v || 'Password is required',
      // v => /^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d).*$/.test(v) || 'Password must contain 8 characters and at least one number and one letter'
    ],
    select: null,
    items: [
      'Админ',
      'Ученик',
      'Репетитор',
    ],
    selectSubj: null,
    subjects: [
        'Русский язык',
        'Математика',
        'Алгебра',
        'Геометрия',
        'Физика',
        'Литература',
        'Обществознание',
        'История',
        'Химия',
    ],
    checkbox: false,
  }),
  methods: {
    register () {
      this.$refs.form1.validate();
      let role = "0";
      let subjid = "0";
      switch (this.$data.select) {
        case "Админ":
          role = "1";
          break;
        case "Ученик":
          role = "2";
          break;
        case "Репетитор":
          role = "3";
          switch (this.$data.selectSubj) {
            case "Русский язык":
              subjid = "1";
              break;
            case "Математика":
              subjid = "2";
              break;
            case "Алгебра":
              subjid = "3";
              break;
            case "Геометрия":
              subjid = "4";
              break;
            case "Физика":
              subjid = "5";
              break;
            case "Литература":
              subjid = "6";
              break;
            case "Обществознание":
              subjid = "7";
              break;
            case "История":
              subjid = "8";
              break;
            case "Химия":
              subjid = "9";
              break;
          }
          break;
      }
      let request = {username: this.$data.email.slice(0, this.$data.email.indexOf("@")),
        name: this.$data.name,
        email: this.$data.email,
        raw_password: this.$data.password,
        password: this.$data.password,
        profile_type: role};
      if (role === "3") {
        request = {username: this.$data.email.slice(0, this.$data.email.indexOf("@")),
          name: this.$data.name,
          email: this.$data.email,
          raw_password: this.$data.password,
          password: this.$data.password,
          profile_type: role,
          subject: subjid};
      }
      axios.post("http://127.0.0.1:8000/backend_app/register/", request)
          .then(response => {
            console.log(response.status);
            // this.resetLogin();
            this.resetRegister();
            this.$data.RegisterShow = false;
            this.$data.SignedInShow=true;
            this.$data.SignedUpShow = false;
            this.$data.InvalidPasswordShow=false;
          })
          .catch(error => console.log(error));
    },
    login () {
      console.log(this.$data.email);
      console.log(this.$data.password);
      this.$refs.form2.validate();
      const request = {};
      axios.get(`http://127.0.0.1:8000/backend_app/checkuser/?email=${this.$data.email}&password=${this.$data.password}`, request)
          .then(response => {
            if (response.status === 200) {
              console.log(response.status);
              this.resetLogin();
              // this.resetRegister();
              this.$data.LoginShow = false;
              this.$data.SignedInShow = false;
              this.$data.SignedUpShow = true;
              this.$data.InvalidPasswordShow = false;
            }
            else{
              this.$data.InvalidPasswordShow=true;
            }
          })
          .catch(error => {
            console.log(error);
            this.$data.InvalidPasswordShow=true;
          });
    },
    resetRegister () {
      this.$refs.form1.reset()
    },
    resetLogin () {
      this.$refs.form2.reset();
      this.$data.InvalidPasswordShow = false;
    },
  },
}
</script>