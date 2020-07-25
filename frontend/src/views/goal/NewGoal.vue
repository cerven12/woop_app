<template>
  <div>
    <br />
    <br />
    <br />
    <br />
    <br />

    <v-container fluid>
      <form-wizard @on-complete="onComplete" color="#4465c0">
        <tab-content title="Goal" icon="ti-user"> </tab-content>
        <tab-content title="Motivation" icon="ti-settings"> </tab-content>
        <tab-content title="GiveUp" icon="ti-check">
          <CreateGiveUp></CreateGiveUp>
        </tab-content>
      </form-wizard>
    </v-container>
  </div>
</template>

<script>
import { FormWizard, TabContent } from "vue-form-wizard";
import "vue-form-wizard/dist/vue-form-wizard.min.css";
import CreateGiveUp from "../goal/giveup/CreateGiveUp.vue";

export default {
  //component code
  components: {
    FormWizard,
    TabContent,
    CreateGiveUp
  },
  data: function () {
    return {
      Goal: {
        goal_title: "",
        goal_description: "",
        criteria: ""
      }
    };
  },
  methods: {
    onComplete: function () {
      alert("Yay. Done!");
    }
  }
};
</script>

<style>
.wizard-header {
  display: none;
}
</style>
