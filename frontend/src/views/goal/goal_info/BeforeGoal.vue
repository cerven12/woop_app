<template>
  <div>
    <!-- Split | Left Side "form"| Right Side "TIps" | -->
    <div id="css-grid">
      <!----------------------------------------------------------------------->
      <!--                       Left Side "form"                         -->
      <!----------------------------------------------------------------------->
      <v-container fluid id="form-area">
        <div id="line">
          <!-- Label -->
          <v-row>
            <v-col cols="10">
              <h4 class="form-group-title">Write it down your Goal.</h4>
            </v-col>
            <v-col>
              <v-btn small color="gray" @click="endEdit">OK!</v-btn>
            </v-col>
          </v-row>

          <!-- Vew Goal Title -->
          <v-row>
            <v-col cols="12">
              <h1 class="goal_title">{{ Goal.goal_title }}</h1>
            </v-col>
          </v-row>

          <!-- Form Goal Tiitle -->
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="Your Goal"
                v-model="Goal.goal_title"
              ></v-text-field>
            </v-col>
          </v-row>

          <!-- Form Goal Description -->
          <v-row>
            <v-col cols="12" md="12">
              <v-textarea
                name="Description"
                label="Description"
                auto-grow
                v-model="Goal.goal_description"
              ></v-textarea>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12" md="12">
              <v-textarea
                name="Success criteria"
                label="Success criteria"
                auto-grow
                v-model="Goal.criteria"
                rows="3"
              ></v-textarea>
            </v-col>
          </v-row>
        </div>
        <br />
      </v-container>

      <!----------------------------------------------------------------------->
      <!--                       Right Side "form"                        -->
      <!----------------------------------------------------------------------->
      <v-container fluid id="tips-area">
        <h1>Tips</h1>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "Goal",
  props: ["Goal"],
  data: function () {
    return {};
  },
  methods: {
    endEdit: function () {
      this.$emit("close");
    }
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  background-color: #f0f0f0;
}

#form-area {
  grid-area: form;
}
#tips-area {
  grid-area: tips;
}

@media all and (max-width: 100000px) {
  #css-grid {
    grid-template-columns: 55% 45%;
    grid-template-areas: "form tips";
    padding: 0px 17%;
  }
}

@media all and (max-width: 1264px) {
  #css-grid {
    grid-template-columns: 100%;
    grid-template-areas:
      "form"
      "tips";
    padding: 0px 13%;
  }
}

@media all and (max-width: 960px) {
  #css-grid {
    padding: 0px 5%;
  }
}

/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.goal_title {
  color: #4465c0;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 36px;
  line-height: 42px;
}

.form-group-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;

  color: #4d4d4d;
}
</style>
