import simpleRestProvider from "ra-data-simple-rest";
import { fetchUtils } from "react-admin";

const httpClient = (url: string, options: any = {}) => {
  const accessToken = localStorage.getItem('accessToken') || '';
  const bearerToken = `Bearer ${accessToken}`;
  if (!options.headers) {
    options.headers = new Headers({ 'Content-type': 'application/json' });
  }
  options.headers.set('Authorization', bearerToken);
  return fetchUtils.fetchJson(url, options);
};


export const dataProvider = simpleRestProvider(
  import.meta.env.VITE_SIMPLE_REST_URL,
  httpClient
);
