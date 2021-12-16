using Microsoft.WindowsAzure.Storage;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace TresureAPIService.Helper
{
	public static class ConnectionString
	{

		public static CloudStorageAccount GetConnectionString()
		{
			string connectionString = string.Format("DefaultEndpointsProtocol=https;AccountName=treasureblob;AccountKey=kV1hDJ+zkWnqoqlJmdFLxjEXCpEFHTU9xTD7Cj+kakxMxRMDfZ1Sj8jxDWFguGX9+Pj8nwb96Yj0LIX4kEjx9w==;EndpointSuffix=core.windows.net");
			return CloudStorageAccount.Parse(connectionString);
		}
	}
}
