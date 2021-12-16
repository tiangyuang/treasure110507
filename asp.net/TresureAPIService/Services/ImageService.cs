using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Web;
using TresureAPIService.Helper;

namespace TresureAPIService.Services
{
	public class ImageService
	{
		private string imageName = Guid.NewGuid().ToString();
		public string Name
        {
			get { return imageName; }
        }
		public async Task<string> UploadImageAsync(HttpPostedFile imageToUpload)
		{
			//+Path.GetExtension(imageToUpload.FileName)
			string imageFullPath = null;
			if (imageToUpload == null || imageToUpload.ContentLength == 0)
			{
				return "error";
			}
			try
			{
				CloudStorageAccount cloudStorageAccount = ConnectionString.GetConnectionString();
				CloudBlobClient cloudBlobClient = cloudStorageAccount.CreateCloudBlobClient();
				CloudBlobContainer cloudBlobContainer = cloudBlobClient.GetContainerReference("treasurecontainer");

				if (await cloudBlobContainer.CreateIfNotExistsAsync())
				{
					await cloudBlobContainer.SetPermissionsAsync(
						new BlobContainerPermissions
						{
							PublicAccess = BlobContainerPublicAccessType.Blob
						}
						);
				}

                CloudBlockBlob cloudBlockBlob = cloudBlobContainer.GetBlockBlobReference(imageName);
				cloudBlockBlob.Properties.ContentType = imageToUpload.ContentType;
				await cloudBlockBlob.UploadFromStreamAsync(imageToUpload.InputStream);

				imageFullPath = cloudBlockBlob.Uri.ToString();
				Console.WriteLine(imageFullPath);
			}
			catch (Exception ex)
			{
				Console.WriteLine("see me ");
				Console.WriteLine(ex.Message);
			}
			return imageFullPath;
		}
	}
}
