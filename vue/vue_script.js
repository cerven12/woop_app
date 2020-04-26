new Vue({
    el: '#app',
    data: function (){
        return {
            goals: {},
            new_goal: '',
            new_task: '',
            isEditGoal: false,
    }
},
    created() {
        this.reloadGoal();
    },
    methods: {
        postGoal: function (goal_title) {
            const vm = this;
            axios.post('http://127.0.0.1:8000/api/v1/goals/',
                { goal_title: goal_title })
        },






        postGoal: function (goal_title) {
            const vm = this;
            axios.post('http://127.0.0.1:8000/api/v1/goals/',
                { goal_title: goal_title })
        },
        deleteGoal: function (id) {
            const vm = this;
            axios.delete('http://127.0.0.1:8000/api/v1/goals/' + id + '/')
                .then(response => { vm.reloadGoal(); })
        },
        updateGoal: function (id, title) {
            const vm = this;
            axios.put('http://127.0.0.1:8000/api/v1/goals/' + id + '/',
                { id: id, goal_title: title })
                .then(response => { vm.isEditGoal = false })
                .catch((error) =>{ console.log(error) })
                .then(response => { vm.reloadGoal(); })
        },
        postTask: function (goal_id, task_title) {
            const vm = this;
            axios.post('http://127.0.0.1:8000/api/v1/goals/'+goal_id+'/'+'tasks'+'/',
                { task_title: task_title , goal: goal_id})
        },
        deleteTask: function (goal_id, task_id) {
            const vm = this;
            axios.delete('http://127.0.0.1:8000/api/v1/goals/'+goal_id+'/'+'tasks'+'/'+task_id+'/')
                .then(response => { vm.reloadGoal(); })
        },
        updateTask: function (goal_id, task_id, task_title) {
            const vm = this;
            axios.put('http://127.0.0.1:8000/api/v1/goals/'+goal_id+'/'+'tasks'+'/'+task_id+'/',
                { task_title: task_tiele , goal: goal_id })
                .then(response => { vm.isEditGoal = false })
                .catch((error) =>{ console.log(error) })
                .then(response => { vm.reloadGoal(); })
        },

        reloadGoal() {
            const vm = this;
            axios.get('http://127.0.0.1:8000/api/v1/goals/')
                .then((response) => { vm.goals = response.data })
        },
    },
}
)