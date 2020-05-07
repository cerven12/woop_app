<template>
  <div id="creategoalcountermeasure">
    <div>
      <!--  worry and idea form -->
      <v-container>
        <v-row>
          <v-col cols="12">
            <h2>▶　挫折をしないために準備する</h2>
          </v-col>
        </v-row>
        <h3>心配事と、それに対する対策を考えておきましょう</h3>
      </v-container>
      <div id="countermeasure" class="input_group">
        <CounterMeasureWorryIdea
          :goal_id="goal_id"
          v-for="n in worryideacomponent"
          v-bind:key="n.id"
        ></CounterMeasureWorryIdea>
        <v-container>
          <v-row>
            <v-col cols="2">
              <v-btn depressed small @click.prevent="addWorryIdeaForm"
                >増やす</v-btn
              ><v-btn depressed small @click.prevent="deleteWorryIdeaForm"
                >減らす</v-btn
              >
            </v-col>
          </v-row>
        </v-container>
      </div>
      <div>
        <!-- reference form -->
        <v-form v-model="valid">
          <v-container>
            <h3>参考にできそうな資料を登録しておきましょう</h3>
            <div
              v-for="(references, index) in refList"
              v-bind:key="references.id"
            >
              <div v-if="index >= 1">
                <v-row>
                  <v-col cols="4">
                    <v-text-field
                      outlined
                      v-model="references.reference_name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="4">
                    <v-text-field
                      outlined
                      v-model="references.reference_use"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="3">
                    <v-text-field
                      outlined
                      v-model="references.reference_source"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="1">
                    <v-btn @click="deleteRefernce(index)" color="error" text
                      >✘</v-btn
                    >
                  </v-col>
                </v-row>
              </div>
              <div v-else>
                <v-row>
                  <v-col cols="4">
                    <v-text-field
                      label="資料"
                      hint="参考にしたい資料を前もって登録しておきましょう"
                      outlined
                      v-model="references.reference_name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="4">
                    <v-text-field
                      label="用途"
                      hint="この資料の用途を書きましょう"
                      outlined
                      v-model="references.reference_use"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="4">
                    <v-text-field
                      label="URL"
                      hint="場所など"
                      outlined
                      v-model="references.reference_source"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </div>
            </div>
            <v-row justify="end">
              <v-col cols="1">
                <v-btn @click="refeadd" depressed small>
                  +
                </v-btn>
              </v-col> </v-row
            ><v-btn outlined @click="refRegister">登録！</v-btn>
          </v-container>
        </v-form>
      </div>
    </div>
  </div>
</template>

<script>
import CounterMeasureWorryIdea from "./CounterMeasureWorryIdea.vue";

export default {
  name: "CreateGoal",
  props: ["goal_id"],
  components: {
    CounterMeasureWorryIdea,
  },

  data: function() {
    return {
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",
      url: "http://127.0.0.1:8000/api/v1/goals/",
      worryideacomponent: 1,
      refList: [
        { reference_name: "", reference_use: "", reference_source: "" },
      ],
    };
  },
  methods: {
    addWorryIdeaForm: function() {
      const vm = this;
      vm.worryideacomponent++;
    },
    deleteWorryIdeaForm: function() {
      const vm = this;
      if (vm.worryideacomponent === 1) {
        console.log(`これ以上は消せないよ`);
      } else {
        vm.worryideacomponent--;
      }
    },
    // worryIdeaRegister: function() {
    //   this.$refs.child.worryIdeaRegister();
    // },

    refeadd: function() {
      const form = {
        reference_name: "",
        reference_use: "",
        reference_source: "",
      };
      this.refList.push(form);
    },
    deleteRefernce: function(index) {
      this.refList.splice(index, 1);
      console.log(this.refList);
    },

    refRegister: function() {
      const vm = this;
      this.refList.forEach(function(refs) {
        // Remove spaces and null strings
        const judgeStrName = refs.reference_name.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        const judgeStrUse = refs.reference_use.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        const judgeStrSource = refs.reference_source.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        if (judgeStrName && judgeStrUse && judgeStrSource) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "references/", {
              goal: vm.goal_id,
              reference_name: refs.reference_name,
              reference_use: refs.reference_use,
              reference_source: refs.reference_source,
            })
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log(`その文字列はだめです`);
        }
      });
    },
  },
};
</script>

<style scoped>
#creategoalcountermeasure {
  background: #f0f0f0;
  /* border: 1px black solid; */
  border-radius: 50px;
  padding: 40px 20px 40px 20px;
  margin: 40px 20px 40px 20px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);

  /* border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255); */
}

#creategoalcountermeasure:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 15px #b9b9b9, -8px -8px 15px #fafafa;
}

h2,
h3 {
  color: rgb(83, 83, 83);
}
</style>

<style>
.v-messages {
  font-size: 15px;
}
.v-messages__message {
  padding-top: 2px;
}
</style>
``
