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
        postGoal: function (title) {
            const vm = this;
            axios.post('http://127.0.0.1:8000/api/v1/Goal/',
                { title: title })
                .then(response => { vm.reloadGoal(); })
        },
        deleteGoal: function (id) {
            const vm = this;
            axios.delete('http://127.0.0.1:8000/api/v1/Goal/' + id)
                .then(response => { vm.reloadGoal(); })
        },
        updateGoal: function (id, title) {
            const vm = this;
            axios.put('http://127.0.0.1:8000/api/v1/Goal/' + id + '/',
                { id: id, title: title })
                .then(response => { vm.isEditGoal = false })
                .catch((error) =>{ console.log(error) })
                .then(response => { vm.reloadGoal(); })
        },
        reloadGoal() {
            const vm = this;
            axios.get('http://127.0.0.1:8000/api/v1/Goal/')
                .then((response) => { vm.goals = response.data })
        },
    },
}
)