import React from "react";
import { Datagrid, DateField, FunctionField, List, TextField } from "react-admin";
import { TINH_TRANG } from "../../contants";

const HeathIndexList: React.FC = () => {

  return (
    <List perPage={50}>
      <Datagrid rowClick="show" >
        <TextField source="id" label="ID" />
        <DateField source="created_at" label="Ngày tiểm tra" showTime />
        <FunctionField label="Kết quả" render={(record: any) => TINH_TRANG[record.ket_qua as string]} />
      </Datagrid>
    </List>
  )
}


export default HeathIndexList;