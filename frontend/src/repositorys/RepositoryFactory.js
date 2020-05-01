import GoalRepository from "./GoalRepository";

const repositories = {
    get: GoalRepository,
    getDetail: GoalRepository,
    post: GoalRepository,
    put: GoalRepository,
    delete: GoalRepository,
}

export const RepositoryFactory ={
    get: name => repositories[name],
    getDetail: name => repositories[name],
    post: name => repositories[name],
    put: name => repositories[name],
    delete: name => repositories[name],
}