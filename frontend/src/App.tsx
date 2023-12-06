import dayjs from 'dayjs';
import 'dayjs/locale/vi';
import React from "react";
import {
  Admin,
  Resource
} from "react-admin";
import Dashboard from "./Dashboard";
import { authProvider } from "./authProvider";
import { dataProvider } from "./dataProvider";
import resourceHeathIndex from "./features/HeathIndex";
dayjs.locale('vi')
export const App: React.FC = () => (
  <Admin title={"Heath Index"}  dataProvider={dataProvider} authProvider={authProvider} requireAuth>
    <Resource {...resourceHeathIndex} />
  </Admin>
);
