SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[train2_ci_datas](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[ci_date] [nvarchar](30) NOT NULL,
	[ci_time] [nvarchar](30) NOT NULL,
	[time_ci_report] [datetime] NOT NULL,
	[batch_no] [nvarchar](20) NOT NULL,
	[order_no] [nvarchar](20) NOT NULL,
	[product_id] [int] NOT NULL,
	[fill_no] [nvarchar](20) NOT NULL,
	[operator_id] [int] NOT NULL,
	[tank1_v1_batch_no] [nvarchar](20) NOT NULL,
	[tank1_v1_trig] [int] NOT NULL,
	[tank1_v1_custom1] [decimal](10, 2) NOT NULL,
	[tank1_v1_custom2] [decimal](10, 2) NOT NULL,
	[tank1_v1_custom3] [decimal](10, 2) NOT NULL,
	[tank1_v1_custom4] [decimal](10, 2) NOT NULL,
	[tank2_a1_batch_no] [nvarchar](20) NOT NULL,
	[tank2_a1_trig] [int] NOT NULL,
	[tank2_a1_t] [decimal](10, 2) NOT NULL,
	[tank2_a1_p] [decimal](10, 2) NOT NULL,
	[tank2_a1_custom1] [decimal](10, 2) NOT NULL,
	[tank2_a1_custom2] [decimal](10, 2) NOT NULL,
	[tank2_a1_custom3] [decimal](10, 2) NOT NULL,
	[tank2_a1_custom4] [decimal](10, 2) NOT NULL,
	[tank3_k1_batch_no] [nvarchar](20) NOT NULL,
	[tank3_k1_trig] [int] NOT NULL,
	[tank3_k1_t] [decimal](10, 2) NOT NULL,
	[tank3_k1_i] [decimal](10, 2) NOT NULL,
	[tank3_k1_s] [decimal](10, 2) NOT NULL,
	[tank3_k1_custom1] [decimal](10, 2) NOT NULL,
	[tank3_k1_custom2] [decimal](10, 2) NOT NULL,
	[tank3_k1_custom3] [decimal](10, 2) NOT NULL,
	[tank3_k1_custom4] [decimal](10, 2) NOT NULL,
	[tank4_k2_batch_no] [nvarchar](20) NOT NULL,
	[tank4_k2_trig] [int] NOT NULL,
	[tank4_k2_t] [decimal](10, 2) NOT NULL,
	[tank4_k2_i] [decimal](10, 2) NOT NULL,
	[tank4_k2_s] [decimal](10, 2) NOT NULL,
	[tank4_k2_custom1] [decimal](10, 2) NOT NULL,
	[tank4_k2_custom2] [decimal](10, 2) NOT NULL,
	[tank4_k2_custom3] [decimal](10, 2) NOT NULL,
	[tank4_k2_custom4] [decimal](10, 2) NOT NULL,
	[tank5_filling1_batch_no] [nvarchar](20) NOT NULL,
	[tank5_filling1_trig] [int] NOT NULL,
	[tank5_filling1_fill_t] [decimal](10, 2) NOT NULL,
	[tank5_filling1_homo_p] [decimal](10, 2) NOT NULL,
	[tank5_filling1_homo_t] [decimal](10, 2) NOT NULL,
	[tank5_filling1_custom1] [decimal](10, 2) NOT NULL,
	[tank5_filling1_custom2] [decimal](10, 2) NOT NULL,
	[tank5_filling1_custom3] [decimal](10, 2) NOT NULL,
	[tank5_filling1_custom4] [decimal](10, 2) NOT NULL,
	[tank6_k3_batch_no] [nvarchar](20) NOT NULL,
	[tank6_k3_trig] [int] NOT NULL,
	[tank6_k3_t] [decimal](10, 2) NOT NULL,
	[tank6_k3_i] [decimal](10, 2) NOT NULL,
	[tank6_k3_s] [decimal](10, 2) NOT NULL,
	[tank6_k3_custom1] [decimal](10, 2) NOT NULL,
	[tank6_k3_custom2] [decimal](10, 2) NOT NULL,
	[tank6_k3_custom3] [decimal](10, 2) NOT NULL,
	[tank6_k3_custom4] [decimal](10, 2) NOT NULL,
	[tank7_filling2_batch_no] [nvarchar](20) NOT NULL,
	[tank7_filling2_trig] [int] NOT NULL,
	[tank7_filling2_fill_t] [decimal](10, 2) NOT NULL,
	[tank7_filling2_homo_p] [decimal](10, 2) NOT NULL,
	[tank7_filling2_homo_t] [decimal](10, 2) NOT NULL,
	[tank7_filling2_custom1] [decimal](10, 2) NOT NULL,
	[tank7_filling2_custom2] [decimal](10, 2) NOT NULL,
	[tank7_filling2_custom3] [decimal](10, 2) NOT NULL,
	[tank7_filling2_custom4] [decimal](10, 2) NOT NULL,
	[remark] [nvarchar](4000) NOT NULL,
	[is_delete] [bit] NOT NULL,
	[is_active] [bit] NOT NULL,
	[created_by] [bigint] NOT NULL,
	[created_at] [datetime] NULL,
	[updated_at] [datetime] NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [product_id]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [operator_id]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank1_v1_trig]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank1_v1_custom1]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank1_v1_custom2]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank1_v1_custom3]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank1_v1_custom4]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank2_a1_trig]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank2_a1_t]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank2_a1_p]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank2_a1_custom1]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank2_a1_custom2]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank2_a1_custom3]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank2_a1_custom4]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank3_k1_trig]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank3_k1_t]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank3_k1_i]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank3_k1_s]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank3_k1_custom1]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank3_k1_custom2]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank3_k1_custom3]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank3_k1_custom4]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank4_k2_trig]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank4_k2_t]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank4_k2_i]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank4_k2_s]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank4_k2_custom1]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank4_k2_custom2]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank4_k2_custom3]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank4_k2_custom4]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank5_filling1_trig]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank5_filling1_fill_t]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank5_filling1_homo_p]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank5_filling1_homo_t]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank5_filling1_custom1]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank5_filling1_custom2]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank5_filling1_custom3]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank5_filling1_custom4]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank6_k3_trig]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank6_k3_t]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank6_k3_i]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank6_k3_s]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank6_k3_custom1]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank6_k3_custom2]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank6_k3_custom3]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank6_k3_custom4]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank7_filling2_trig]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank7_filling2_fill_t]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank7_filling2_homo_p]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank7_filling2_homo_t]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank7_filling2_custom1]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank7_filling2_custom2]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank7_filling2_custom3]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [tank7_filling2_custom4]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('0') FOR [is_delete]
GO
ALTER TABLE [dbo].[train2_ci_datas] ADD  DEFAULT ('1') FOR [is_active]
GO
ALTER TABLE [dbo].[train2_ci_datas]  WITH CHECK ADD  CONSTRAINT [train2_ci_datas_created_by_foreign] FOREIGN KEY([created_by])
REFERENCES [dbo].[users] ([id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[train2_ci_datas] CHECK CONSTRAINT [train2_ci_datas_created_by_foreign]
GO
