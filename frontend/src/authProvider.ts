import { AuthProvider } from "react-admin";

/**
 * This authProvider is only for test purposes. Don't use it in production.
 */
export const authProvider: AuthProvider = {
    login: ({ username, password }) => {
        const request = new Request(import.meta.env.VITE_SIMPLE_REST_URL+'/auth/login', {
            method: 'POST',
            body: JSON.stringify({ username, password }),
            headers: new Headers({ 'Content-Type': 'application/json' }),
        });
        return fetch(request)
            .then(response => {
                if (response.status < 200 || response.status >= 300) {
                    throw new Error(response.statusText);
                }
                return response.json();
            })
            .then(auth => {
                localStorage.setItem('accessToken', auth.token);
            })
            .catch(() => {
                throw new Error('Network error')
            });
    },
    logout: () => {
        localStorage.removeItem("accessToken");
        return Promise.resolve();
      },
      checkError: () => Promise.resolve(),
      checkAuth: () =>
        localStorage.getItem("accessToken") ? Promise.resolve() : Promise.reject(),
      getPermissions: () => {
        return Promise.resolve(undefined);
      },
      getIdentity: async () => {
        const accessToken = localStorage.getItem('accessToken') || '';
        const bearerToken = `Bearer ${accessToken}`;
        const request = await fetch(import.meta.env.VITE_SIMPLE_REST_URL+'/auth/get-identity', {
          headers: new Headers({ 'Authorization': bearerToken }),
        });
        const response = await request.json()
        response.fullName = response.fullname;
        delete response.fullname;
        return response;
      },
};

export default authProvider;
