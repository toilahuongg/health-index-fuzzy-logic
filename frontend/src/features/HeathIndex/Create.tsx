import React from "react";
import { Create, NumberInput, SimpleForm, required } from "react-admin";
import { Grid } from '@mui/material';
export const HeathIndexCreate: React.FC = () => {
  return (
    <Create title="Tạo phiếu">
      <SimpleForm>
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <NumberInput min={0} source="chieu_cao" label="Chiều cao (cm)" validate={required()} fullWidth />
          </Grid>
          <Grid item xs={6}>
            <NumberInput min={0} source="can_nang" label="Cân nặng (kg)" validate={required()} fullWidth />
          </Grid>
        </Grid>
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <NumberInput min={0} source="mat" label="Thị lực (/20)" validate={required()} fullWidth />
          </Grid>
          <Grid item xs={6}>
            <NumberInput min={0} source="suc_nghe" label="Sức nghe 2 tai (m)" validate={required()} fullWidth />
          </Grid>
        </Grid>
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <NumberInput min={0} source="rang" label="Mất răng (cái)" validate={required()} fullWidth />
          </Grid>
          <Grid item xs={6}>
            <NumberInput min={0} source="mach" label="Nhịp tim (lần/phút)" validate={required()} fullWidth />
          </Grid>
        </Grid>
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <NumberInput min={0} source="co_rut" label="Co rút ngón chân/tay" validate={required()} fullWidth />
          </Grid>
        </Grid>
      </SimpleForm>
    </Create>
  )
};


export default HeathIndexCreate;