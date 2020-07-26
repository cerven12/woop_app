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
              <h2 class="message-title">Lets preparations for not give up.</h2>
            </v-col>
          </v-row>

          <!----------------------------------------------------------------------->
          <!--            Obstacle & Countermeasure.                 -->
          <!----------------------------------------------------------------------->
          <h3 class="category-title">Obstacle & Countermeasur.</h3>
          <transition-group name="form" tag="div">
            <div
              v-for="(worries, worries_index) in Worries"
              :key="worries_index"
            >
              <!-- If it's two or more Worry Model forms, show ✘, and label and hint is hide of Worry. Idea Model form. -->
              <template v-if="worries_index >= 1">
                <v-row>
                  <v-col cols="11" md="11">
                    <v-textarea
                      rows="1"
                      auto-grow
                      v-model="worries.worries"
                    ></v-textarea>
                  </v-col>
                  <v-col cols="1">
                    <v-btn
                      @click="deleteWorryIdeaForm(worries_index)"
                      text
                      depressed
                      height="55"
                      color="error"
                    >
                      ✘
                    </v-btn>
                  </v-col>
                </v-row>

                <!-- Idea Model Form -->
                <transition-group name="form" tag="div">
                  <div
                    v-for="(ideas, ideas_index) in worries.ideas"
                    :key="ideas_index"
                  >
                    <v-row justify="end">
                      <v-col cols="2"></v-col>
                      <!--The second and subsequent Idea model forms belonging to the Worry model form will not be labeled or named. -->
                      <template v-if="ideas_index >= 1">
                        <v-col cols="9">
                          <v-textarea
                            rows="1"
                            auto-grow
                            v-model="ideas.idea"
                          ></v-textarea>
                        </v-col>

                        <v-col cols="1">
                          <v-btn
                            @click="deleteIdeaForm(worries_index, ideas_index)"
                            text
                            depressed
                            height="55"
                            color="error"
                          >
                            ✘
                          </v-btn>
                        </v-col>
                      </template>

                      <!-- First Idea Model form -->
                      <template v-else>
                        <v-col cols="9">
                          <v-textarea rows="1" auto-grow v-model="ideas.idea">
                          </v-textarea>
                        </v-col>
                        <v-col cols="1"> </v-col>
                      </template>
                    </v-row>
                  </div>
                </transition-group>
              </template>
              <!-- This is the end of the Worry Model form after 2. -->

              <!-- First Worry Model form -->
              <template v-else>
                <v-row>
                  <v-col cols="12">
                    <v-textarea
                      name="障壁"
                      label="Obstacle"
                      hint=""
                      rows="1"
                      auto-grow
                      v-model="worries.worries"
                    ></v-textarea>
                  </v-col>
                </v-row>

                <!-- Idea Model Form -->
                <transition-group name="form" tag="div">
                  <div
                    v-for="(ideas, ideas_index) in worries.ideas"
                    :key="ideas_index"
                  >
                    <v-row justify="end">
                      <v-col cols="2"></v-col>

                      <!-- If it's two or more Idea Model forms, show ✘, and label and hint is hide. -->
                      <template v-if="ideas_index >= 1">
                        <v-col cols="9">
                          <v-textarea rows="1" auto-grow v-model="ideas.idea">
                          </v-textarea>
                        </v-col>
                        <v-col cols="1">
                          <v-btn
                            @click="deleteIdeaForm(worries_index, ideas_index)"
                            text
                            depressed
                            height="55"
                            color="error"
                          >
                            ✘
                          </v-btn>
                        </v-col>
                      </template>
                      <!-- This is the end of the Idea Model form after 2.  -->

                      <!-- First Idea Model form -->
                      <template v-else>
                        <v-col>
                          <v-textarea
                            name="解決策"
                            label="Countermeasure."
                            hint=""
                            rows="1"
                            auto-grow
                            v-model="ideas.idea"
                          ></v-textarea></v-col
                      ></template>
                      <!-- This is the end of the First Idea Model form. -->
                    </v-row>
                  </div>
                </transition-group>
              </template>

              <v-row justify="end">
                <v-col cols="1">
                  <v-btn depressed small @click="addIdeaForm(worries_index)">
                    ＋
                  </v-btn>
                </v-col>
              </v-row>
            </div>
          </transition-group>

          <v-row>
            <v-col>
              <v-btn @click="addWorryIdeaForm" text depressed>＋</v-btn>
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
  name: "Goal",

  data: function () {
    return {
      valid: "",
      Worries: [{ worries: "", ideas: [{ idea: "" }] }],
      parentWorryId: "",
      refList: [{ reference_name: "", reference_use: "", reference_source: "" }]
    };
  },

  methods: {
    //  ------------------------------------------------------------
    //                   Form  Increase
    //  ------------------------------------------------------------
    addWorryIdeaForm: function () {
      const form = { worries: "", ideas: [{ idea: "" }] };
      this.Worries.push(form);
    },
    addIdeaForm: function (worries_id) {
      const form = { idea: "" };
      this.Worries[worries_id].ideas.push(form);
    },
    //  ------------------------------------------------------------
    //                   Form Delete
    //  ------------------------------------------------------------
    deleteWorryIdeaForm: function (worry_id) {
      this.Worries.splice(worry_id, 1);
    },
    deleteIdeaForm: function (worries_id, ideas_id) {
      this.Worries[worries_id].ideas.splice(ideas_id, 1);
    },
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

@media all and (max-width: 960px){
  #css-grid{
    padding: 0px 5%;
  }
}

/*   ------------------------------------------------------------
                          Transition
 ------------------------------------------------------------*/
.countermeasure-enter-active,
.countermeasure-leave-active {
  transition: opacity 0.3s;
}
.countermeasure-enter,
.countermeasure-leave-to {
  opacity: 0;
}

/* add(delete) form */
.form-enter-active {
  animation: fadeInUp 0.3s;
  transition: opacity 0.3s;
}
.form-leave-active {
  animation: fadeInUp 0.3s reverse;
  transition: opacity 0.3s;
}
.form-enter,
.form-leave-to {
  opacity: 0;
}

@keyframes fadeInUp {
  0% {
    transform: translateX(20px);
    opacity: 0;
  }
  60% {
    opacity: 0.3;
  }
  100% {
    transform: translateX(0px);
    opacity: 1;
  }
}

/*   ------------------------------------------------------------
                            Font Desiign
------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 28px;
  line-height: 40px;
  color: #4465c0;
}

.category-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 40px;
  color: #3c3d3d;
}
</style>
