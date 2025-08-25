class ApiRouteConfig {
  #task = '/task';

  task(path: string = '') {
    return `${this.#task}${path ? `/${path}/` : '/'}`;
  }
}
export const apiRoutes = new ApiRouteConfig();
