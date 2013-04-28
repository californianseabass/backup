//
//  main.c
//  backup
//
//  Created by Eric Sebastian Soto on 4/26/13.
//  Copyright (c) 2013 Eric Sebastian Soto. All rights reserved.
//

/*
 * Four general steps for discovering devices:
 * Discover devices using libusb_get_device_list().
 * Choose the device that you want to operate, and call libusb_open().
 * Unref all devices in the discovered device list.
 * Free the discovered device list.
 */

#include <stdio.h>
#include <libusb.h>

void printdev(libusb_device *dev);

int main(int argc, const char * argv[])
{

    libusb_device **devs; //pointer to pointer of device, used to retrieve a list of devices
    libusb_device_handle *dev_handle; //a device handle
    libusb_context *ctx = NULL; //a libusb session
    int r; //for return values
    ssize_t cnt; //holding number of devices in list
    r = libusb_init(&ctx); //initialize the library for the session we just declared
    if(r < 0) {
        printf("Init Error\n"); //there was an error
        return 1;
    }
    
    libusb_set_debug(ctx, 3); //set verbosity level to 3, as suggested in the documentation
    
    
    cnt = libusb_get_device_list(ctx, &devs); //get the list of devices
    if(cnt < 0) {
        printf("get device error\n"); //there was an error
        return 1;
    }
    printf("devices in list\n");
    ssize_t i; //for iterating through the list
    libusb_device *src;
    for(i = 0; i < cnt; i++) {
        printdev(devs[i]); //print specs of this device

    }
    libusb_free_device_list(devs, 1); //free the list, unref the devices in it
    libusb_exit(ctx); //close the session
    return 0;
}


void printdev(libusb_device *dev) {
    struct libusb_device_descriptor desc;
    int r = libusb_get_device_descriptor(dev, &desc);
    if (r < 0) {
        printf("failed to get device descriptor\n");
        return;
    }
    if (desc.idVendor == 1452) return;
    if (desc.bDeviceClass != 0) return;
    printf("Number of possible configurations: %d\n", (int)desc.bNumConfigurations);
    printf("Device Class: %d\n", (int)desc.bDeviceClass);
    printf("VendorID: %d\n", desc.idVendor);
    printf("ProductID: %d\n", desc.idProduct);
    printf("Device Address: %d\n",  libusb_get_device_address(dev));
    printf("Serial Number: %d\n", desc.iSerialNumber);
    printf("Bus number: %d\n", libusb_get_bus_number(dev));
    struct libusb_config_descriptor *config;
    libusb_get_config_descriptor(dev, 0, &config);
    printf("Interfaces: %d\n", config->bNumInterfaces);
    const struct libusb_interface *inter;
    const struct libusb_interface_descriptor *interdesc;
    const struct libusb_endpoint_descriptor *epdesc;
    for(int i=0; i<(int)config->bNumInterfaces; i++) {
        inter = &config->interface[i];
        printf("Number of alternate settings: %d\n", inter->num_altsetting);
        for(int j=0; j<inter->num_altsetting; j++) {
            interdesc = &inter->altsetting[j];
            printf("Interface Number: %d | ", (int)interdesc->bInterfaceNumber);
            printf("Number of endpoints: %d | ", (int)interdesc->bNumEndpoints);
            for(int k=0; k<(int)interdesc->bNumEndpoints; k++) {
                epdesc = &interdesc->endpoint[k];
                printf("Descriptor Type: %d |", (int)epdesc->bDescriptorType);
                printf("EP Address: %d\n", (int)epdesc->bEndpointAddress);
            }
        }
        
    }
    
    libusb_free_config_descriptor(config);
}
