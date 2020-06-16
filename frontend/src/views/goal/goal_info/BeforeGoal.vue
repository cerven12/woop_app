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
            <v-col cols="12">
              <h4 class="form-group-title">Write it down your Goal.</h4>
            </v-col>
          </v-row>

          <!-- Vew Goal Title -->
          <v-row>
            <v-col cols="12">
              <h1 class="goal_title">{{ goal_title }}</h1>
            </v-col>
          </v-row>

          <!-- Form Goal Tiitle -->
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="Your Goal"
                v-model="goal_title"
              ></v-text-field>
            </v-col>
          </v-row>

          <!-- Form Goal Description -->
          <v-row>
            <v-col cols="12" md="12">
              <v-textarea
                name="Description"
                label="Description"
                rows="1"
                auto-grow
                v-model="goal_description"
              ></v-textarea>
            </v-col>
          </v-row>
        </div>
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
  data: function() {
    return {
      goal_title:
        "Create Web SPA Todo App  at use Django Rest Framework and Vue.",
      goal_description: "",
      valid: "",
    };
  },
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 55% 45%;
  grid-template-areas: "form tips";
  background-color: #f0f0f0;
}

#form-area {
  grid-area: form;
}
#tips-area {
  grid-area: tips;
}

/*   ------------------------------------------------------------
                            Form Design
 ------------------------------------------------------------*/
#line {
  margin: 80px;
  padding: 60px 100px;
  border-radius: 77px;
  box-shadow: 5px 5px 5px #b9b9b9, -5px -5px 5px #fafafa;
}

/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.goal_title {
  color: #5f75b0;
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
  font-size: 18px;
  line-height: 28px;

  color: #3c3d3d;
}
</style>
