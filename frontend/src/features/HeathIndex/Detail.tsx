import { Grid } from '@mui/material';
import { ArcElement, CategoryScale, Chart as ChartJS, ChartOptions, ChartType, Colors, Legend, LineElement, LinearScale, PointElement, TimeScale, Title, SubTitle, Tooltip } from "chart.js";
import 'chartjs-adapter-moment';
import zoomPlugin from 'chartjs-plugin-zoom';
import moment from 'moment';
import React from "react";
import { FunctionField, NumberField, Show, SimpleShowLayout, required, useGetList, useRecordContext } from "react-admin";
import { Doughnut, Line } from 'react-chartjs-2';
import { TINH_TRANG } from '../../contants';

ChartJS.register(ArcElement, CategoryScale, LinearScale, PointElement, LineElement, TimeScale, zoomPlugin, Tooltip, Legend, Colors, Title, SubTitle);
const Result = () => {
  const record = useRecordContext();
  return (
    <>
      {record && (
        <Doughnut
          options={{
            plugins: {
              title: {
                display: true,
                text: record.ket_qua >= 4 ? 'Bạn đủ điều kiện để nhập ngũ' : 'Bạn không đủ điều kiện để nhập ngũ',
                font: { size: 20 }
              },
              subtitle: {
                display: true,
                text:[`Chỉ số sức khoẻ: ${record.ket_qua}`, `Tình trạng: ${TINH_TRANG[record.ket_qua as string]}`]
              }
            }
          }}
          data={{
            labels: ['Loại 1', 'Loại 2', 'Loại 3', 'Loại 4', 'Loại 5', 'Loại 6'],
            datasets: [{
              label: 'Độ chính xác (%)',
              data: [record.point1, record.point2, record.point3, record.point4, record.point5, record.point6]
            }],
          }}
        />
      )}
    </>
  )
}

type MinMaxProp = {
  min: number;
  max: number;
}

const ChartList = () => {
  const record = useRecordContext();
  const { data } = useGetList(
    'heath-index',
    {
      pagination: { page: 1, perPage: 1000000 },
    }
  );

  if (!data || !record) return <></>
  const renderOptions = (props?: MinMaxProp): ChartOptions<ChartType> => ({
    scales: {
      x: {
        type: 'time',
        time: {
          unit: 'day', // Adjust the time unit as needed (day, month, year, etc.)
          displayFormats: {
            day: 'YYYY-MM-DD',
          },
        },
        min: moment(record.created_at).subtract(100, 'days').format('YYYY-MM-DD'),
        max: moment(record.created_at).add(100, 'days').format('YYYY-MM-DD')
      },
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Value',
        },
        ...props
      },
    },
    plugins: {
      zoom: {
        zoom: {
          wheel: {
            enabled: true,
            modifierKey: 'ctrl'
          },
          pinch: {
            enabled: true,
          },
          mode: 'xy',
          drag: {
            enabled: true,
            modifierKey: 'alt'
          }
        },
        pan: {
          enabled: true,
          modifierKey: 'ctrl',
          mode: 'xy'
        },
      }
    },

    elements: {
      ...ChartJS.defaults.elements,
      point: {
        ...ChartJS.defaults.elements.point,
        backgroundColor: (context) => {
          // Lấy chỉ mục của ngày trong mảng labelsThang
          const index = context.dataIndex;

          // Kiểm tra nếu ngày là ngày cụ thể bạn muốn thay đổi màu
          const isTargetDate = data[index].created_at === record.created_at

          // Trả về màu sắc tương ứng
          return isTargetDate ? 'red' : 'blue';
        },
        borderWidth: (context) => {
          // Lấy chỉ mục của ngày trong mảng labelsThang
          const index = context.dataIndex;

          // Kiểm tra nếu ngày là ngày cụ thể bạn muốn thay đổi màu
          const isTargetDate = data[index].created_at === record.created_at

          // Trả về màu sắc tương ứng
          return isTargetDate ? 20 : 0;
        }
      }
    }
  });
  return (
    <Grid container spacing={2}>
      <Grid item xs={12} md={6}>
        <Line
          data={{
            datasets: [{
              label: 'Cân nặng',
              data,
            }],
          }}
          options={{
            parsing: {
              xAxisKey: 'created_at',
              yAxisKey: 'can_nang'
            },
            ...renderOptions({ min: 50, max: 100 }) as any
          }}
        />
      </Grid>
      <Grid item xs={12} md={6}>
        <Line
          data={{
            datasets: [{
              label: 'Thị lực',
              data,
            }],
          }}
          options={{
            parsing: {
              xAxisKey: 'created_at',
              yAxisKey: 'mat'
            },
            ...renderOptions() as any
          }}
        />
      </Grid>
      <Grid item xs={12} md={6}>
        <Line
          data={{
            datasets: [{
              label: 'Sức nghe',
              data,
            }],
          }}
          options={{
            parsing: {
              xAxisKey: 'created_at',
              yAxisKey: 'suc_nghe'
            },
            ...renderOptions() as any
          }}
        />
      </Grid>
      <Grid item xs={12} md={6}>
        <Line
          data={{
            datasets: [{
              label: 'Mất răng',
              data,
            }],
          }}
          options={{
            parsing: {
              xAxisKey: 'created_at',
              yAxisKey: 'rang'
            },
            ...renderOptions() as any
          }}
        />
      </Grid>
      <Grid item xs={12} md={6}>
        <Line
          data={{
            datasets: [{
              label: 'Nhịp tim',
              data,
            }],
          }}
          options={{
            parsing: {
              xAxisKey: 'created_at',
              yAxisKey: 'mach'
            },
            ...renderOptions({ min: 60, max: 120 }) as any
          }}
        />
      </Grid>
      <Grid item xs={12} md={6}>
        <Line
          data={{
            datasets: [{
              label: 'Co rút chân tay',
              data,
            }],
          }}
          options={{
            parsing: {
              xAxisKey: 'created_at',
              yAxisKey: 'co_rut'
            },
            ...renderOptions() as any
          }}
        />
      </Grid>
    </Grid>
  )
}
export const HeathIndexShow: React.FC = () => {

  return (
    <Show>
      <Grid container spacing={2}>
        <Grid item xs={12} md={8}>
          <SimpleShowLayout>
            <NumberField min={0} source="chieu_cao" label="Chiều cao (cm)" validate={required()} />
            <NumberField min={0} source="can_nang" label="Cân nặng (kg)" validate={required()} />
            <NumberField min={0} source="mat" label="Thị lực (/20)" validate={required()} />
            <NumberField min={0} source="suc_nghe" label="Sức nghe (m)" validate={required()} />
            <NumberField min={0} source="rang" label="Mất răng (cái)" validate={required()} />
            <NumberField min={0} source="mach" label="Nhịp tim (lần/phút)" validate={required()} />
            <FunctionField label="Co rút ngón chân/tay" render={(record: any) => record.co_rut || 0} />
          </SimpleShowLayout>
        </Grid>
        <Grid item xs={12} md={4}>
          <SimpleShowLayout>
            <Result />
          </SimpleShowLayout>
        </Grid>
        <Grid item xs={12}>
          <SimpleShowLayout>
            <ChartList />
          </SimpleShowLayout>
        </Grid>
      </Grid>
    </Show>
  )
};


export default HeathIndexShow;