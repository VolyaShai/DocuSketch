import pandas as pd
from matplotlib import pyplot as plt

deviation_df = pd.read_json('./deviation.json')


class PlotsDraw:

    def draw_function_gt_rb(self, doc_df):
        gt_rb_df = pd.concat([doc_df['gt_corners'].value_counts(),
                              doc_df["rb_corners"].value_counts()], axis=1).reset_index()
        gt_rb_df.columns = ['value', 'gt_corners', 'rb_corners']
        gt_rb_df.plot(x='value', y=['gt_corners', 'rb_corners'], kind='bar',
                      ylabel='count', figsize=(12, 5), grid=True, logy=True)
        plt.savefig("plots/gt_rb_corners_bar_log.png")
        print("draw_function_gt_rb paths: plots/gt_rb_corners_bar_log.png")

    def draw_function_mean(self, doc_df):
        mean_df = pd.concat([doc_df['mean'],
                             doc_df["floor_mean"],
                             doc_df["ceiling_mean"]], axis=1).reset_index()
        mean_df.columns = ['value', 'mean', 'floor_mean', 'ceiling_mean']
        mean_df.plot(x='value', y=['mean', 'floor_mean', 'ceiling_mean'], kind='line', linestyle='dotted',
                     ylabel='count', alpha=0.8, figsize=(12, 5), grid=True)
        plt.savefig("plots/mean_df_line.png")
        print("draw_function_mean paths: plots/mean_df_line.png")


a = PlotsDraw()
a.draw_function_gt_rb(deviation_df)
a.draw_function_mean(deviation_df)
