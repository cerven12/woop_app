<template>
  <div>
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
              <v-btn small color="gray" @click="editTask">OK!</v-btn>
            </v-col>
          </v-row>

          <!-- Vew Goal Title -->
          <v-row>
            <v-col cols="12">
              <h1 class="task_title">{{ TaskInfo.task_title }}</h1>
            </v-col>
          </v-row>

          <!-- Form Goal Tiitle -->
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="Your Goal"
                v-model="TaskInfo.task_title"
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
                v-model="TaskInfo.task_description"
              ></v-textarea>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12" md="12">
              <v-textarea
                name="Success criteria"
                label="Success criteria"
                auto-grow
                v-model="TaskInfo.criteria"
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
import api from "@/services/api";

export default {
  name: "Task",
  props: ["TaskInfo", "OriginalTaskInfo"],

  methods: {
    endEdit: function () {
      this.$emit("close");
    },

    editTask: function () {
      const vm = this;
      let goalId = this.$route.params.id;
      let taskId = vm.TaskInfo.task_id;
      let postData = { }; // in Changed Data
      let isChanged = 0; // Use post methods if over 1.
      // add postData if change values.
      if (vm.OriginalTaskInfo.task_title != vm.TaskInfo.task_title) {
        postData["task_title"] = vm.TaskInfo.task_title;
        isChanged++;
      }
      if (
        (vm.OriginalTaskInfo.task_description != vm.TaskInfo.task_description)
      ) {
        postData["task_description"] = vm.TaskInfo.task_description;
        isChanged++;
      }
      if ((vm.OriginalTaskInfo.criteria != vm.TaskInfo.criteria)) {
        postData["criteria"] = vm.TaskInfo.criteria;
        isChanged++;
      }

      if (isChanged >= 1) {
        api
          .patch(`goals/${goalId}/tasks/${taskId}/`, postData, {
            useCredentails: true
          })
          .then(function (response) {
            // for next edit
            vm.OriginalTaskInfo.task_title = vm.TaskInfo.task_title;
            vm.OriginalTaskInfo.task_description = vm.TaskInfo.task_description;
            vm.OriginalTaskInfo.criteria = vm.TaskInfo.criteria;
            console.log(response)
          })
          .catch(function (error) {
            console.log(error);
          });
      }
      // switch component. `close` is parent component.
      vm.$emit("close");
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
.task_title {
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
